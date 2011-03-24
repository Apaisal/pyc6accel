'''
Created on Mar 4, 2011

@author: anol
'''
from threading import Thread
import socket
import random
import re
import time


class RTSP:
    '''
    Real Time Streaming Protocol Class
    '''
    info = {}
    uriformat = ("%(schema)s://%(ipaddress)s:%(port)s/%(absolutepath)s?res=%(res)s&x0=0&y0=0&x1=%(width)s&y1=%(height)s&ssn=%(ssn)s&qp=%(qp)s&bitrate=%(bitrate)s")
    def __init__(self, ip, res = 'full', size = (1280, 720)):
        '''
        Initialize
        '''
        self.info['schema'] = 'rtsp'
        self.info['version'] = '1.0'
        self.info['ipaddress'] = ip
        self.info['port'] = 554
        self.info['absolutepath'] = 'h264.sdp'
        self.info['res'] = res
        self.info['width'] = size[0]
        self.info['height'] = size[1]
        self.info['qp'] = 16
        self.info['bitrate'] = 65536
        self.info['fps'] = 15
        self.info['ssn'] = random.randint(1, 65535)
        self.CSeq = 1
        self.TCPSocket = None
        self.UDPSocket = None
        self.UDPFeedbackSocket = None
        self.buffer_size = 102400
        self.receiveData = None
        self.info['session'] = None
        self.server_port = []
        self.client_port = ['48872', '48873']

    def Connect(self, address, proto = 'tcp'):
        ''''''
        try:
            if proto == 'tcp':
#                if self.UDPSocket is not None:
#                    self.UDPSocket.close()
                self.TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
                self.TCPSocket.connect(address)
            elif proto == 'udp':
#                if self.TCPSocket is not None:
#                    self.TCPSocket.close()
                self.UDPSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
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

    def DESCRIBE(self, uri):
        ''''''
        requestline = 'DESCRIBE %(uri)s %(schema)s/%(version)s\r\nCSeq: %(cseq)s\r\nAccept: application/sdp\r\n\r\n' \
        % {'uri':uri, 'schema':self.info['schema'].upper(), 'version':self.info['version'], 'cseq':self.CSeq}
        try:
            self.TCPSocket.send(requestline)
            self.TCPSocket.recv(self.buffer_size)
            self.receiveData = self.TCPSocket.recv(self.buffer_size)
            print self.receiveData
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
            self.TCPSocket.recv(self.buffer_size)

            self.receiveData = self.TCPSocket.recv(self.buffer_size)
            print self.receiveData
            session = re.findall(r'(?<=session: )\d*', self.receiveData, re.IGNORECASE)
            serv_port = re.findall(r'(?<=server_port=)\d*[-]\d*', self.receiveData, re.IGNORECASE)
            if len(session) > 0 :
                self.info['session'] = session[0][0]
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
            self.TCPSocket.recv(self.buffer_size)
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
            self.TCPSocket.recv(self.buffer_size)
            self.receiveData = self.TCPSocket.recv(self.buffer_size)
            print self.receiveData
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
            self.TCPSocket.recv(self.buffer_size)
            self.receiveData = self.TCPSocket.recv(self.buffer_size)
            print self.receiveData
            self.CSeq += 1
        except socket.error, msg:
            if self.TCPSocket is not None:
                self.TCPSocket.close()
            raise socket.error, msg

    def getRTP(self):
        ''''''
        try:
            self.receiveData = self.UDPSocket.recv(self.buffer_size)
            print 'packet size : %d' % (len(self.receiveData))
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
    ip = '158.108.47.118'
    rtsp = RTSP(ip)
    uri = rtsp.getURI()
    rtsp.Connect((ip, 554), 'tcp')
    rtsp.DESCRIBE(uri)
    rtsp.SETUP(uri)
    rtsp.PLAY(uri)
    rtsp.Connect(('', int(rtsp.client_port[0])), 'udp')
    # Start timer
    strtime = time.clock()
#    print strtime
    while True:
        # Receive H264 packet
        rtsp.getRTP()

        # Check timer for send rtcp feedback every 5-10 sec
        deltatime = time.clock() - strtime

        if deltatime > 0.06:
            print deltatime
            rtsp.sendFeedback((ip, int(rtsp.server_port[1])))
            strtime = time.clock()

    rtsp.Close()
    rtsp = None
