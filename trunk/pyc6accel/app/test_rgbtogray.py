import cv
import pyc6accel

lenaimg = cv.LoadImage('test_files/VGA.jpg', cv.CV_LOAD_IMAGE_COLOR)
cv.Scale(lenaimg, lenaimg, 1);

def test(img):
    print 'RGB to Gray Method'
    outrgb2y = cv.CreateImage(cv.GetSize(img), img.depth, 1)
    t = cv.GetTickCount()
    pyc6accel.CvtColor(img, outrgb2y, cv.CV_RGB2GRAY)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "pyc6accel rgb2g detection time = %g ms" % msec
    cv.SaveImage('test_files/result_rgb2g_pyc6accel.jpg', outrgb2y)
#    fd.write(str(msec) + '\t')
#    t = cv.GetTickCount()
#    cv.CvtColor(img, outrgb2y, cv.CV_RGB2GRAY)
#    t = cv.GetTickCount() - t
#    msec = t / (cv.GetTickFrequency() * 1000.)
#    print "opencv rgb2g detection time = %g ms" % msec
#    cv.SaveImage('test_files/result_rgb2g_opencv.jpg', outrgb2y)
#    fd.write(str(msec) + '\t')

if __name__ == '__main__' :
    ''''''
    for i in range(1):
        test(lenaimg)