#! /usr/bin/env python
#! -*- code:utf-8 -*-
'''
Created on Jul 24, 2010

@author: anol
'''
import urllib2
#import urllib
import Image
import cv
#import socket

class IPCamera(object):
    def __init__(self, url = 'http://158.108.47.118/mjpeg?res=full', param = None):
        self.url = url
        self.param = param
        self.state = 0
        self.buffer = ''
        self.limit = 8192

    def Start(self):
        try:
            self.fp = urllib2.build_opener().open(self.url)
        except urllib2.URLError :
            print u"""Check connection"""
        self.state = True

    def Stop(self):
        self.fp.close()
        self.state = 0

    def NextFrame(self):
        if self.state:
            count = 0
            begin = 0
            t = 0;
            self.fp = urllib2.build_opener().open(self.url)
            while (count == 0) :
                try :
                    temp = self.fp.read(self.limit)
                    self.buffer += temp
                    boundary = self.buffer.find(r"""--fbdr""")
                    count = self.buffer.count(r"""--fbdr""")
                    print "Attempt Number ", t
                    t += 1
#                    cv.WaitKey(50)
#                    break
                except ValueError:
#                    stop and restart
                    self.Stop()
                    self.Start()
                    self.buffer = ''
                    self.NextFrame()
            print "Find the Begining of the Mjpeg Stream"
#            We find the begining from the frame
#            Move the pointer to the location of the begining of the frame
            begin = boundary + 36
#            Next wait until we get EOF '\xFF\xD9'
            count = 0;
            t = 0;
            while (count == 0) :

                temp = self.fp.read(self.limit)
                self.buffer += temp
                boundary = self.buffer.find("\xFF\xD9")
                count = self.buffer.count("\xFF\xD9")
                print "Attempt Number ", t
                t += 1


            #We find the end of the file
            end = boundary + 2
            buff2 = self.buffer[begin:end]
            self.buffer = buff2
            imPIL = Image.frombuffer("RGB", (1600, 1184), buff2, 'jpeg', "RGB", None);
            self.buffer = ''
            im = cv.CreateImageHeader(imPIL.size, cv.IPL_DEPTH_8U, 3)
            cv.SetData(im, imPIL.tostring())
            return im



#import nmap, re, httplib, cv, os, Image, StringIO
#
#
##pattern
#length_pattern = re.compile('(\d+$)')
#date_pattern = re.compile('(\d.*?\d)')
#
#def readLine(res):
#	line = ''
#	while res.status == 200:
#		chr = res.read(1)
#		if not chr in ['\n']:
#			line += chr
#		else:
#			break
#	return line.strip()
#
#def getLength(res):
#	line = readLine(res)
#	if line.find('length') == -1:
#		return getLength(res)
#	return int(length_pattern.search(line).group(0))
#
#def getDate(res):
#	line = readLine(res)
#	return date_pattern.search(line).group(0)
#
#def getType(res):
#	line = readLine(res)
#	return line
#
#class IPCamera():
#	'''
#	IP Camera Class
#	'''
#
#	def __init__(self):
#		'''		im = Image.fromstring("RGB", (640, 480), buff)
#		Initialize IP Camera Object
#		'''
#		self.nm = nmap.PortScanner()
#		self.hosts = None
##		self.scan_ip_network()
#		self.connect = None
#
#	def scan_ip_network(self, ipnetwork = '192.168.1.0/24', port = '8481'):
#		print "Start scan ip camera...\n"
#		#(default ip network: 192.168.1.0/24)
#		self.nm.scan(hosts = ipnetwork , ports = port)
#		#filter ip alive 
#		hosts_list = [host for host in self.nm.all_hosts() if self.nm[host]['status']['state'] == 'up']
#		#filter specify port open (default port: 8481)
#		self.hosts = [ host for host in hosts_list if self.nm[host]['tcp'][int(port)]['state'] == 'open']
#		if self.hosts.__len__() > 0:
#			print "Found IP Camera : %s" % self.hosts[0]
#		else:
#			print "Not found IP Camera"
#
#	def createCapture(self):
#		path = 'mjpeg.cgi' #image.jpg
#		self.connect = httplib.HTTPConnection(self.hosts[0])
#		self.connect.request('GET', path)
#		self.res = self.connect.getresponse()
#
#	def closeCapture(self):
#		self.connect.close()
#
#	def getImage(self):
#
#		#get header information
#		length = getLength(self.res)
#		getDate(self.res)
#		getType(self.res)
#		readLine(self.res)
#		buff = self.res.read(length)
#		im = Image.open(StringIO.StringIO(buff))
#		cv_im = cv.CreateImageHeader(im.size, im.bits, im.layers)	#RGB
#
#		cv.SetData(cv_im, im.tostring(), im.size[0] * 3)
#		cv_im = cv.DecodeImage(cv_im, cv.CV_LOAD_IMAGE_COLOR)
#		small_img = cv.CreateImage((cv.Round(im.size[0] / 2),
#                   cv.Round (im.size[1] / 2)), im.bits, im.layers)
#		cv.Resize(cv_im, small_img)
#		cv.CvtColor(small_img, small_img, cv.CV_BGR2RGB)
#		return small_img
#
#if __name__ == '__main__':
#	camera = IPCamera()
#	#find camera @ lab
#	camera.scan_ip_network("158.108.47.0/24")
#	camera.createCapture()
#	img = camera.getImage()
