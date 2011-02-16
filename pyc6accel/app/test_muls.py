import cv
import pyc6accel
import test

lenaimg = cv.LoadImage('test_files/VGA.png', cv.CV_LOAD_IMAGE_GRAYSCALE)
cv.Scale(lenaimg, lenaimg, 1);

def test(img):
    print 'MulS Scalar Method'
    muls_img = cv.CreateImage(cv.GetSize(img), img.depth, img.nChannels)
    t = cv.GetTickCount()
    pyc6accel.MulS(img, 0.8, muls_img)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "pyc6accel Muls detection time = %g ms" % (t / (cv.GetTickFrequency() * 1000.))
    cv.SaveImage('test_files/result_muls_pyc6accel.png', muls_img)
    
#    fd.write(str(msec) + '\t')
#
#    muls_opencv = cv.CreateImage(cv.GetSize(img), img.depth, img.nChannels)
#    cv.SetData(adds_pyc6accel, ret, img.width)
#    t = cv.GetTickCount()
#    cv.Mul(img, 100, muls_opencv)
#    t = cv.GetTickCount() - t
#    msec = t / (cv.GetTickFrequency() * 1000.)
#    print "opencv Muls detection time = %g ms" % (t / (cv.GetTickFrequency() * 1000.))
#    cv.SaveImage('test_files/result_muls_opencv.png', muls_opencv)
#    fd.write(str(msec) + '\t')
    
if __name__ == '__main__' :
    ''''''
    for i in range(1):
        test(lenaimg)