import cv
import pyc6accel

lenaimg = cv.LoadImage('test_files/VGA.png', cv.CV_LOAD_IMAGE_GRAYSCALE)
cv.Scale(lenaimg, lenaimg, 1);

def test(img):
    print 'Sub Scalar Method'
    out_img = cv.CreateImage(cv.GetSize(img), img.depth, img.nChannels)
    t = cv.GetTickCount()
    pyc6accel.SubS(img, 70, out_img)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "pyc6accel subs detection time = %g ms" % (t / (cv.GetTickFrequency() * 1000.))
    cv.SaveImage('test_files/result_subs_pyc6accel.png', out_img)
#    fd.write(str(msec) + '\t')
    #
    cv.Zero(out_img)
    t = cv.GetTickCount()
    cv.SubS(img, 70, out_img)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "opencv subs detection time = %g ms" % (t / (cv.GetTickFrequency() * 1000.))
    cv.SaveImage('test_files/result_subs_opencv.png', out_img)
#fd.write(str(msec) + '\t')
    
if __name__ == '__main__' :
    ''''''
    for i in range(1):
        test(lenaimg)