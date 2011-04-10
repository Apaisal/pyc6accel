'''
Created on Mar 4, 2011

@author: anol
'''
#from threading import Thread
import socket
import random
import re
import time
import string
import binascii
import base64

import gobject, pygst
pygst.require("0.10")
import gst

class SDPMessage:
    def __init__(self):
        self.Message = {}
        self.Message['v'] = 'Session Description Protocol Version'
        self.Message['o'] = 'Owner/Creator and Session Identifier'
        self.Message['s'] = 'Session name'
        self.Message['t'] = 'Time Description, time active'
        self.Message['m'] = 'Media Description, name and address'
        self.Message['a'] = 'Media Attribute'


class RTSPResponse:
     def __init__(self, context):
         self.raw = context
         data = self.raw.split('\r\n\r\n')
         self.Header = data[0].strip().splitlines()
         self.Payload = data[1].strip().splitlines()


class SDPElement:
    def __init__(self, name, value):
        ''''''
        msg = SDPMessage().Message
        self.description = msg[name]
        self.raw = value.split(':')
        self.shortname = name
        self.field = None
        self.value = None
        self.format = None
        self.parameters = None

        if len(self.raw) == 1:
            self.value = self.raw[0]
        else:
            self.field = self.raw[0]
            self.value = self.raw[1].split()
            self.format = self.value[0]
            if len(self.value) > 1:
                self.parameters = self.value[1].split(';')


    def getName(self):
        return self.shortname
    name = property(getName, None, None, None)

    def getPacketizationMode(self):
        if self.parameters is None or len(self.parameters) == 1:
            return None
        for para in self.parameters:
            key, value = para.split('=', 1)
            if key.find('packetization') == 0:
                return value

    def getProfileLevelID(self):
        if self.parameters is None or len(self.parameters) == 1:
            return None
        for para in self.parameters:
            key, value = para.split('=', 1)
            if key.find('profile') == 0:
                return value

    def getSpropParameterSet(self):
        if self.parameters is None or len(self.parameters) == 1:
            return None
        for para in self.parameters:
            key, value = para.split('=', 1)
            if key.find('sprop') == 0:
                return value

    PacketizationMode = property(getPacketizationMode, None, None, None)
    ProfileLevelID = property(getProfileLevelID, None, None, None)
    SpropParameterSet = property(getSpropParameterSet, None, None, None)

class SDP:
    def __init__(self, context):
        '''
        '''
        self.raw = context
        self.elements = []

        for line in self.raw:
            type = line[0]
            self.elements.append(SDPElement(type, line[2:]))

    def getPacketizationMode(self):
        for element in self.elements:
            if element.PacketizationMode is None:
                continue
            return element.PacketizationMode

    def getProfileLevelID(self):
        for element in self.elements:
            if element.ProfileLevelID is None:
                continue
            return element.ProfileLevelID

    def getSpropParameterSet(self):
        for element in self.elements:
            if element.SpropParameterSet is None:
                continue
            return element.SpropParameterSet

    PacketizationMode = property(getPacketizationMode, None, None, None)
    ProfileLevelID = property(getProfileLevelID, None, None, None)
    SpropParameterSet = property(getSpropParameterSet, None, None, None)

class RTPdecH264:
    def __init__(self, pkgm, profile, parameterset):
        ''''''
        self.packetization_mode = int(pkgm)
        self.profile = profile
        self.parameterset = parameterset.split(',')
        self.profile_idc = None
        self.profile_iop = None
        self.level_idc = None
        self.CodecExtraData = None
        self.CodecData = None

    def fmtp_config_h264(self):
        codecdata = ''

        if (self.profile != '' or self.profile != None) and len(self.profile) == 6 :
            self.profile_idc = int(self.profile[0:1], 16);
            self.profile_iop = int(self.profile[2:3], 16);
            self.level_idc = int(self.profile[4:5], 16);
            print "RTP Profile IDC: %x Profile IOP: %x Level: %x\n" % (self.profile_idc, self.profile_iop, self.level_idc)

        if self.parameterset != None :
            start_seq = '\x00' * 2 + '\x01'
            for value in self.parameterset:
                dec = base64.b64decode(value)
                codecdata += start_seq
#                for h in range(0, len(dec), 2):
                codecdata += dec
                codecdata += '\x00' * 8
        self.CodecExtraData = codecdata

    def h264_handle_packet(self, buf):
        ''''''
        nal = buf[0];
        type = ord(nal) & 0x1f;
        result = 0;
        start_sequence = '\x00' * 2 + '\x01'
        data = ''
        if type >= 1 and type <= 23:
            type = 1 # simplify the case. (these are all the nal types used internally by the h264 codec)

        if type == 28:  #FU-A (fragmented nal)
            pack = buf[1:] #skip the fu_indicator
            # these are the same as above, we just redo them here for clarity...
            fu_indicator = nal;
            fu_header = pack[0]; #// read the fu_header.
            start_bit = ord(fu_header) >> 7;
#//            uint8_t end_bit = (fu_header & 0x40) >> 6;
            nal_type = ord(fu_header) & 0x1f;

#            // reconstruct this packet's true nal; only the data follows..
            reconstructed_nal = ord(fu_indicator) & 0xe0  #// the original nal forbidden bit and NRI are stored in this packet's nal;
            reconstructed_nal |= nal_type;

#            // skip the fu_header...
            pack = pack[1:]
            if(start_bit):
#                // copy in the start sequence, and the reconstructed nal....
                data += start_sequence
                data += chr(reconstructed_nal);
            data += pack

            self.CodecData = data
            return data

class RTSP:
    '''
    Real Time Streaming Protocol Class
    '''

    def __init__(self, ip, res = 'full', size = (1280, 720)):
        '''
        Initialize
        '''
        self.info = {}
        self.uriformat = ("%(schema)s://%(ipaddress)s:%(port)s/%(absolutepath)s?res=%(res)s&x0=0&y0=0&x1=%(width)s&y1=%(height)s&ssn=%(ssn)s&qp=%(qp)s&bitrate=%(bitrate)s")
        self.UserAgent = 'Bacom Co,Ltd. (Visset Streaming Media Library) 2011'

        self.info['schema'] = 'rtsp'
        self.info['version'] = '1.0'
        self.info['ipaddress'] = ip
        self.info['port'] = 554
        self.info['absolutepath'] = 'h264.sdp'
        self.info['res'] = res
        self.info['width'] = size[0]
        self.info['height'] = size[1]
        self.info['qp'] = 20
        self.info['bitrate'] = 65536
        self.info['fps'] = 30
        self.info['ssn'] = random.randint(1, 65535)
        self.info['session'] = None
        self.CSeq = 1
        self.TCPSocket = None
        self.UDPSocket = None
        self.UDPFeedbackSocket = None
        self.buffer_size = 1500
        self.receiveData = None
        self.server_port = []
        self.client_port = ['48872', '48873']
        self.h264data = {}
        self.ReponseStatus = ''
        self.RTSPResponse = None
        self.SDP = None
        self.RTPH264dec = None

    def Connect(self, address, proto = 'tcp'):
        ''''''
        try:
            if proto == 'tcp':
#                if self.UDPSocket is not None:
#                    self.UDPSocket.close()
                self.TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.TCPSocket.connect(address)
            elif proto == 'udp':
#                if self.TCPSocket is not None:
#                    self.TCPSocket.close()
                self.UDPSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#                self.UDPSocket.setblocking(True)
                self.UDPSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.UDPSocket.bind(address)
#                self.UDPSocket.connect(address)
        except socket.error, msg:
            raise socket.error, msg

    def Close(self):
        ''''''
        if self.TCPSocket is not None:
            self.TCPSocket.close()
        if self.UDPSocket is not None:
            self.UDPSocket.close()
        if self.UDPFeedbackSocket is not None:
            self.UDPFeedbackSocket.close()

    def getURI(self):
        ''''''
        return self.uriformat % self.info


    def reponse_status(self):
        self.ReponseStatus = self.receiveData.split()[1]
        return self.ReponseStatus


    def recv_data(self):
        self.receiveData = self.TCPSocket.recv(self.buffer_size)

    def DESCRIBE(self, uri):
        ''''''
        requestline = 'DESCRIBE %(uri)s %(schema)s/%(version)s\r\nCSeq: %(cseq)s\r\nAccept: application/sdp\r\nUser-Agent: %(useragent)s\r\n\r\n' \
        % {'uri':uri, 'schema':self.info['schema'].upper(), 'version':self.info['version'], 'cseq':self.CSeq, 'useragent': self.UserAgent}
        try:
            self.TCPSocket.send(requestline)
            self.recv_data()
            if self.reponse_status() == '200':
                self.recv_data()
                self.RTSPResponse = RTSPResponse(self.receiveData)
                self.SDP = SDP(self.RTSPResponse.Payload)
                self.RTPH264dec = RTPdecH264(self.SDP.PacketizationMode, self.SDP.ProfileLevelID, self.SDP.SpropParameterSet)
                self.RTPH264dec.fmtp_config_h264()
                self.CSeq += 1
        except socket.error, msg:
            if self.TCPSocket is not None:
                self.TCPSocket.close()
            raise socket.error, msg

    def SETUP(self, uri):
        ''''''
        requestline = 'SETUP %(uri)s/trackID=1 %(schema)s/%(version)s\r\nCSeq: %(cseq)s\r\nTransport: RTP/AVP;unicast;client_port=48872-48873\r\n\r\n' \
        % {'uri':uri, 'schema':self.info['schema'].upper(), 'version':self.info['version'], 'cseq':self.CSeq}
        try:
            self.TCPSocket.send(requestline)
            self.recv_data()
            if self.reponse_status() == '200':
                self.recv_data()
                print self.receiveData
                session = re.findall(r'(?<=session: )\d*', self.receiveData, re.IGNORECASE)
                serv_port = re.findall(r'(?<=server_port=)\d*[-]\d*', self.receiveData, re.IGNORECASE)
                if len(session) > 0 :
                    self.info['session'] = session[0]
                if len(serv_port) > 0 :
                    self.server_port = serv_port[0].split('-')
                self.CSeq += 1
        except socket.error, msg:
            if self.TCPSocket is not None:
                self.TCPSocket.close()
            raise socket.error, msg

    def PLAY(self, uri):
        ''''''
        requestline = 'PLAY %(uri)s %(schema)s/%(version)s\r\nCSeq: %(cseq)s\r\nSession: %(session)s\r\nRange: npt=0.000-\r\n\r\n' \
        % {'uri':uri, 'schema':self.info['schema'].upper(), 'version':self.info['version'], 'cseq':self.CSeq, 'session': self.info['session']}
        try:
            self.TCPSocket.send(requestline)
            print self.TCPSocket.recv(self.buffer_size)
            self.receiveData = self.TCPSocket.recv(self.buffer_size)
            print self.receiveData
            self.CSeq += 1
        except socket.error, msg:
            if self.TCPSocket is not None:
                self.TCPSocket.close()
            raise socket.error, msg

    def PAUSE(self, uri):
        ''''''
        requestline = 'PAUSE %(uri)s %(schema)s/%(version)s\r\nCSeq: %(cseq)s\r\nSession: %(session)s\r\n\r\n' \
        % {'uri':uri, 'schema':self.info['schema'].upper(), 'version':self.info['version'], 'cseq':self.CSeq, 'session': self.info['session']}
        try:
            self.TCPSocket.send(requestline)
            self.CSeq += 1
        except socket.error, msg:
            if self.TCPSocket is not None:
                self.TCPSocket.close()
            raise socket.error, msg

    def TEARDOWN(self, uri):
        ''''''
        requestline = 'TEARDOWN %(uri)s %(schema)s/%(version)s\r\nCSeq: %(cseq)s\r\nSession: %(session)s\r\n\r\n' \
        % {'uri':uri, 'schema':self.info['schema'].upper(), 'version':self.info['version'], 'cseq':self.CSeq, 'session': self.info['session']}
        try:
            self.TCPSocket.send(requestline)
            self.CSeq += 1
        except socket.error, msg:
            if self.TCPSocket is not None:
                self.TCPSocket.close()
            raise socket.error, msg

    def getRTP_Payload(self):
        ''''''
        try:
            self.receiveData = self.UDPSocket.recv(self.buffer_size)
            print 'packet size : %d' % (len(self.receiveData))
            if len(self.receiveData) > 0:
                return self.RTPH264dec.h264_handle_packet(self.receiveData[12:])

        except socket.error, msg:
            if self.UDPSocket is not None:
                self.UDPSocket.close()
            raise socket.error, msg
#        print len(self.receiveData)
    def sendFeedback(self, address):
        data = 'Feedback'
        try:
            if self.UDPFeedbackSocket is None:
                self.UDPFeedbackSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
                self.UDPFeedbackSocket.bind(('', int(self.client_port[1])))
            self.UDPFeedbackSocket.sendto(data, address)
        except socket.error, msg:
            if self.UDPFeedbackSocket is not None:
                self.UDPFeedbackSocket.close()
            raise socket.error, msg

#    def setQP(self, value):
#        if ((value < 4) | (value > 51)):
#            raise ValueError('QP parameter must be integer between 4 and 51')
#        self.info['qp'] = value
#        re.sub(r"&bitrate=%(bitrate)s", '', self.uriformat)
#        self.uriformat += '&qp=%(qp)s'
#
#    def setBitrate(self, value):
#        if ((value < 0) | (value > 65536)):
#            raise ValueError('QP parameter must be integer between 4 and 51')
#        self.info['bitrate'] = value
#        re.sub(r"&qp=%[(]qp[)]s", '', self.uriformat)
#        self.uriformat += '&bitrate=%(bitrate)s'


if __name__ == '__main__':
    ip = '158.108.47.75'
    rtsp = RTSP(ip)
    uri = rtsp.getURI()
    rtsp.Connect((ip, 554), 'tcp')
    rtsp.DESCRIBE(uri)
    rtsp.SETUP(uri)
    rtsp.PLAY(uri)
    rtsp.Connect(('', int(rtsp.client_port[0])), 'udp')
    count = 0
    max = 5000
    # Start timer
    strtime = time.clock()
#    print strtime
#    fp = rtsp.UDPSocket.makefile('r', rtsp.buffer_size)
    fd = open('cam.264', 'wb')
    fd.write(rtsp.RTPH264dec.CodecExtraData)
    while (True):

        # Receive H264 packet
#        frame = ''
#        while True:
        rtsp.getRTP_Payload()




        fd.write(rtsp.RTPH264dec.CodecData)
#        if dsp == None :
            #import pyc6accel as dsp
#        dec = dsp.H264Decode(fd)
#        print "Finish\n"
    #    print "H264 to UYUV size %\n" % (len(dec[0:10]))
#        exit(0)

#        fp.flush()
#        fd.flush()

        # Check timer for send rtcp feedback every 5-10 sec
        deltatime = time.clock() - strtime

        if deltatime > 0.05:
            print deltatime
            rtsp.sendFeedback((ip, int(rtsp.server_port[1])))
            strtime = time.clock()
        if count >= max and binascii.hexlify(rtsp.receiveData[1]) == 'e0':
            count = 0
            break
        count += 1
    fd.close()
#    fp.close()
#    rtsp.Connect((ip, 554), 'tcp')
#    rtsp.PAUSE(uri)
    rtsp.TEARDOWN(uri)
    rtsp.Close()
    rtsp = None
    print "Finish\n"
