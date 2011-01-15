import cv
import pyc6accel

lenaimg = cv.LoadImage('test_files/lena.jpg', cv.CV_LOAD_IMAGE_GRAYSCALE)
cv.Scale(lenaimg, lenaimg, 1);

def test(img):
    print 'Threshold Method'
    out_pyc6accel = cv.CreateImage(cv.GetSize(img), img.depth, img.nChannels)
    t = cv.GetTickCount()
    pyc6accel.Threshold(img, out_pyc6accel, 80, pyc6accel.THRESH_LESS2MIN)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "pyc6accel Threshold detection time = %g ms" % msec
    cv.SaveImage('test_files/result_Threshold_pyc6accel_THRESH_LESS2MIN.jpg', out_pyc6accel)
#    fd.write(str(msec) + '\t')
#    out_opencv = cv.CreateImage(cv.GetSize(img), img.depth, img.nChannels)
#    t = cv.GetTickCount()
#    cv.Threshold(img, out_opencv, value, 255, cv.CV_THRESH_TOZERO_INV)
#    t = cv.GetTickCount() - t
#    msec = t / (cv.GetTickFrequency() * 1000.)
#    print "opencv Threshold detection time = %g ms" % msec
#    cv.SaveImage('test_files/result_Threshold_opencv.jpg', out_opencv)
#    fd.write(str(msec) + '\t')
    
if __name__ == '__main__' :
    ''''''
    for i in range(1):
        test(lenaimg)