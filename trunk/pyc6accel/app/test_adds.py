import cv
import test
import pyc6accel

lenaimg = cv.LoadImage('test_files/VGA.png', cv.CV_LOAD_IMAGE_GRAYSCALE)
cv.Scale(lenaimg, lenaimg, 1);

def test(img):
    print 'Add Scalar Method'
    adds_img = cv.CreateImage(cv.GetSize(img), img.depth, img.nChannels)
    t = cv.GetTickCount()
    pyc6accel.AddS(img, 100, adds_img)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "pyc6accel adds detection time = %g ms" % (t / (cv.GetTickFrequency() * 1000.))
    cv.SaveImage('test_files/result_adds_pyc6accel.png', adds_img)
#    fd.write(str(msec) + '\t')
#
    pyc6accel.ReleaseImage(adds_img)
    adds_opencv = cv.CreateImage(cv.GetSize(img), img.depth, img.nChannels)
#    cv.SetData(adds_pyc6accel, ret, img.width)
    t = cv.GetTickCount()
    cv.AddS(img, 100, adds_opencv)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "opencv adds detection time = %g ms" % (t / (cv.GetTickFrequency() * 1000.))
    cv.SaveImage('test_files/result_adds_opencv.png', adds_opencv)
#    fd.write(str(msec) + '\t')
    pyc6accel.ReleaseImage(adds_opencv)


if __name__ == '__main__' :
    ''''''
    for i in range(1):
        test(lenaimg)
    pyc6accel.ReleaseImage(lenaimg)
