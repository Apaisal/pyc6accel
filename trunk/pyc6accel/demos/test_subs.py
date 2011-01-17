import cv
import pyc6accel

lenaimg = cv.LoadImage('test_files/lena.jpg', cv.CV_LOAD_IMAGE_GRAYSCALE)
cv.Scale(lenaimg, lenaimg, 1);

def test(img):
    print 'Sub Scalar Method'
    out_img = cv.CreateImage(cv.GetSize(img), img.depth, img.nChannels)
    t = cv.GetTickCount()
    pyc6accel.SubS(img, 70, out_img)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "pyc6accel subs detection time = %g ms" % (t / (cv.GetTickFrequency() * 1000.))
    cv.SaveImage('test_files/result_subs_pyc6accel.jpg', out_img)
#    fd.write(str(msec) + '\t')
    #
    #    adds_opencv = cv.CreateMat(img.rows, img.cols, cv.CV_8UC1)
    #    cv.SetData(adds_pyc6accel, ret, img.width)
#    t = cv.GetTickCount()
#    cv.AddS(img, 100, out_img)
#    t = cv.GetTickCount() - t
#    msec = t / (cv.GetTickFrequency() * 1000.)
#    print "opencv subs detection time = %g ms" % (t / (cv.GetTickFrequency() * 1000.))
#    cv.SaveImage('test_files/result_subs_opencv.jpg', out_img)
#fd.write(str(msec) + '\t')
    
if __name__ == '__main__' :
    ''''''
    for i in range(10):
        test(lenaimg)