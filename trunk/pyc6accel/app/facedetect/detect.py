'''
Created on Aug 14, 2010

@author: anol
'''
import cv, time
#import pyc6accel as dsp

class detect():
    '''
    classdocs
    '''


    def __init__(self, cascade):
        '''
        Constructor
        '''
        self.cascade = cascade
        self.historyimage = None

    def detect_and_draw(self, image):
        # Parameters for haar detection
        # From the API:
        # The default parameters (scale_factor=2, min_neighbors=3, flags=0) are tuned 
        # for accurate yet slow object detection. For a faster operation on real video 
        # images the settings are: 
        # scale_factor=1.2, min_neighbors=2, flags=CV_HAAR_DO_CANNY_PRUNING, 
        # min_size=<minimum possible face size

        min_size = (3, 3)
        image_scale = 1.2
        haar_scale = 1.5
        min_neighbors = 2
        haar_flags = cv.CV_HAAR_SCALE_IMAGE #cv.CV_HAAR_DO_CANNY_PRUNING #cv.CV_HAAR_DO_ROUGH_SEARCH | cv.CV_HAAR_FEATURE_MAX
        gray = cv.CreateImage((image.width, image.height), 8, 1)
        small_img = cv.CreateImage((cv.Round(image.width / image_scale),
                   cv.Round (image.height / image_scale)), 8, 1)

        # convert color input image to grayscale
        cv.CvtColor(image, gray, cv.CV_BGR2GRAY)
#        dsp.CvtColor(image, gray, dsp.CV_RGB2GRAY)
#         scale input image for faster processing
        cv.Resize(gray, small_img, cv.CV_INTER_LINEAR)

        cv.EqualizeHist(small_img, small_img)

        if(self.cascade):
            start = cv.GetTickCount()
            faces = cv.HaarDetectObjects(small_img, self.cascade, cv.CreateMemStorage(0)
            , haar_scale \
            , min_neighbors \
            , haar_flags \
            , min_size \
            )
            interval = cv.GetTickCount() - start
            print "detection time = %gms" % (interval / (cv.GetTickFrequency()*1000.))
            scale = 1
            if faces:
                for ((x, y, w, h), n) in faces:
                    # the input to cv.HaarDetectObjects was resized, so scale the 
                    # bounding box of each face and convert it to two CvPoints
                    pt1 = (int(x * image_scale), int(y * image_scale))
                    pt2 = (int((x + w) * image_scale), int((y + h) * image_scale))
                    cv.Rectangle(image, pt1, pt2, cv.RGB(255, 0, 0), 1, 8, 0)


    def detect_object(self, image):
        if self.historyimage is None:
            self.historyimage = cv.CloneImage(image)
        cv.UpdateMotionHistory(image, self.historyimage, 2, 1)
        print self.lastimage
