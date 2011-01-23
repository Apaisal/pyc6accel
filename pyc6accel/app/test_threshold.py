import cv
import pyc6accel

lenaimg = cv.LoadImage('test_files/VGA.jpg', cv.CV_LOAD_IMAGE_GRAYSCALE)
cv.Scale(lenaimg, lenaimg, 1);

def test(img, thres):
    print 'Threshold Method'
    out_pyc6accel = cv.CreateImage(cv.GetSize(img), img.depth, img.nChannels)
    t = cv.GetTickCount()
    pyc6accel.Threshold(img, out_pyc6accel, 80, thres)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "pyc6accel Threshold % s detection time = %g ms" % (thres,msec)
    cv.SaveImage('test_files/result_Threshold_pyc6accel_%s.jpg' % thres, out_pyc6accel)
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
        test(lenaimg,pyc6accel.THRESH_GREATER2MAX)
        test(lenaimg,pyc6accel.THRESH_GREATER2THRES)
        test(lenaimg,pyc6accel.THRESH_LESS2MIN)
        test(lenaimg,pyc6accel.THRESH_LESS2THRES)