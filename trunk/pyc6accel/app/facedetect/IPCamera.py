import urllib2
import urllib
import Image
import cv
import socket
from threading import Thread
from threading import RLock
import time
import sys

class IPCamera(Thread):
    def __init__(self, url , res = 'full', quality = 10, upleft = (0, 0), lowright = (1280, 1024), param = None):
        #find new corners
        upleft = ((upleft[0] / 64) * 64, (upleft[1] / 64) * 64)
        lowright = ((lowright[0] / 64) * 64, (lowright[1] / 64) * 64)
        if res == 'full' : #Full Resolution
            self.url = url + "/mjpeg?res=" + res + "&quality=" + format(quality)
            self.url += "&x0=" + format(upleft[0]) + "&y0=" + format(upleft[1])
            self.url += "&x1=" + format(lowright[0]) + "&y1=" + format(lowright[1])
            self.imSize = (lowright[0] - upleft[0], lowright[1] - upleft[1])
        else:
            self.url = url + "/mjpeg?res=" + 'half' + "&quality=" + format(quality)
            self.url += "&x0=" + format(upleft[0]) + "&y0=" + format(upleft[1])
            self.url += "&x1=" + format(lowright[0]) + "&y1=" + format(lowright[1])
            self.imSize = ((lowright[0] - upleft[0]) / 2, (lowright[1] - upleft[1]) / 2)
        print "url =" + self.url
        self.param = param
        self.state = 0
        self.buffer = ''
        self.buffer2 = ''
        self.limit = 1024
        self.im = cv.CreateImageHeader(self.imSize , cv.IPL_DEPTH_8U, 3)
        self.rlock = RLock()
        self.bufferImageNumber = 0
        self.bufferNumber = 0
        self.hasImage = False
        self.fp = None

        Thread.__init__(self)


    def openPort(self):
        try:
            self.fp = urllib2.build_opener().open(self.url)
#            self.fp.close()
#            self.fp = None
        except urllib2.URLError :
            print u"""Check connection"""
        self.state = True


    def Stop(self):
        self.state = 0


    def run(self) :
        if self.state:
            count = 0
            begin = 0
            findBeginFrame = False
            self.fp = urllib2.build_opener().open(self.url)
            print "Thread Starts"
            self.threadStarted = True
            SearchForJpegHeader = False
            while (self.state) : # in the running mode
                try :
                    temp = self.fp.read(self.limit)
                except :
                    self.fp = urllib2.build_opener().open(self.url)
                    self.buffer = ''
                    temp = ''
                    findBeginFrame = False
                self.buffer += temp
                if not(findBeginFrame) :
                    count = self.buffer.count(r"""--fbdr""")
                    if (count > 0) : # the begining of the frame found
                        #clear everything before the begining of the frame
                        boundary = self.buffer.find(r"""--fbdr""")
                        lenBuffer = len(self.buffer)
                        self.buffer = self.buffer[boundary + 6:lenBuffer + 1]
                        findBeginFrame = True
                        strtime = time.clock()
                    else : # still not find the begining of the frame flush out
                        self.buffer = ''
                else :
                    # here the begining of the frame has found wait until
                    # getting a new one
                    # we receive a new one unil we find a new header
                    count = self.buffer.count(r"""--fbdr""")

                    if (count > 0) : # new frame is found
                        #put the full Jpeg image into buffer 2
                        begin = self.buffer.find("\xff\xd8") #Begining of Jpeg data
                        end = self.buffer.find("\xff\xd9")
                        if (begin == -1) | (end == -1) : #one of them is missing
                            self.buffer = ''
                            findBeginFrame = False # Search for new frame
                        else : # has complete Jpeg data
                            self.buffer2 = self.buffer[begin:(end + 1)]
                            stptime = time.clock()
                            print "Total download per frame is %f seconds" % (stptime - strtime)
                            self.hasImage = True
                            self.bufferNumber += 1
                            #print "We have successfully captured "+format(self.bufferNumber) + "images"
                            lenBuffer = len(self.buffer)
                            self.buffer = self.buffer[end + 2:lenBuffer + 1]
                            findBeginFrame = False
        print "Thread Stoped"
        self.fp.close()

    def getImage(self) :
        if (self.hasImage == False) :
            #print "Image is not ready,"
            return None
        else :
            #print "Creating images"
            strtime = time.clock()
            if (self.bufferNumber <> self.bufferImageNumber) :
                getImThread = cvImageFromJPEGBuffer(self.buffer2, self.imSize)
                getImThread.start()
                while (getImThread.isImageRead() == False) :
                    cv.WaitKey(2)
                if (getImThread.imError == False) :
                    self.im = getImThread.getImage()
                    self.bufferImageNumber = self.bufferNumber
            stptime = time.clock()
            print "Image Convertion takes %f seconds" % (stptime - strtime)
        return self.im


    def NextFrameImage(self):
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
                   # cv.WaitKey(50)
                    #break
                except ValueError:
                    #stop and restart
                    self.Stop()
                    self.Start()
                    self.buffer = ''
                    self.NextFrame()
            print "Find the Begining of the Mjpeg Stream"
            #We find the begining from the frame
            #Move the pointer to the location of the begining of the frame
            begin = boundary + 36
            #Next wait until we get EOF '\xFF\xD9'
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


class cvImageFromJPEGBuffer(Thread) :
     def __init__(self, buff, size, param = None):
         self.buffer = buff;
         self.imSize = size
         self.imout = cv.CreateImage(size, cv.IPL_DEPTH_8U, 3)
         self.imReady = False
         self.imError = False
         Thread.__init__(self)

     def convertToCvImage(self) :
         try :
             imPIL = Image.frombuffer("RGB", self.imSize, self.buffer, 'jpeg', "RGB", None);
             im = cv.CreateImage(self.imSize, cv.IPL_DEPTH_8U, 3)
             cv.SetData(im, imPIL.tostring())
             cv.CvtColor(im, self.imout, cv.CV_BGR2RGB)
             self.imReady = True
             self.imError = False
         except : # can't convert image
             print "Jpeg decoder error" + self.buffer
             fp = file("tempimage.jpg", 'w')
             fp.write(self.buffer)
             fp.close()
             sys.exit(1)
             im = None
             self.imReady = True
             self.imError = True




     def run(self) :
         self.convertToCvImage()

     def isImageRead(self) :
         return self.imReady

     def getImage(self) :
         if (self.imReady) :
             if (self.imError == False) :
                 return self.imout
             else :
                 return None
         else :
             return None





