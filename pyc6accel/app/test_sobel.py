import cv
import pyc6accel

lenaimg = cv.LoadImage('test_files/VGA.jpg', cv.CV_LOAD_IMAGE_GRAYSCALE)
cv.Scale(lenaimg, lenaimg, 1);

def test(img):
    print 'Sobel Method'
    sobel_pyc6accel = cv.CreateImage(cv.GetSize(img), img.depth, img.nChannels)
    t = cv.GetTickCount()
    ret = pyc6accel.Sobel(img, sobel_pyc6accel, 3)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "pyc6accel sobel detection time = %gms" % (t / (cv.GetTickFrequency() * 1000.))
    cv.SaveImage('test_files/result_sobel_pyc6accel.jpg', sobel_pyc6accel)
    
#    fd.write(str(msec) + '\t')
#
#    sobel_opencv_16 = cv.CreateImage(cv.GetSize(img), cv.IPL_DEPTH_16S, img.nChannels)
#    sobel_opencv_8 = cv.CreateImage(cv.GetSize(img), img.depth, img.nChannels)
#    t = cv.GetTickCount()
#    cv.Sobel(img, sobel_opencv_16, 1, 1, 3)
#    cv.ConvertScaleAbs(sobel_opencv_16, sobel_opencv_8, 1, 0)
#    t = cv.GetTickCount() - t
#    msec = t / (cv.GetTickFrequency() * 1000.)
#    print "opencv sobel detection time = %gms" % (t / (cv.GetTickFrequency() * 1000.))
#    cv.SaveImage('test_files/result_sobel_opencv.jpg', sobel_opencv_8)
#    fd.write(str(msec) + '\t')
    
if __name__ == '__main__' :
    ''''''
    for i in range(1):
        test(lenaimg)