import cv
import pyc6accel

lenaimg = cv.LoadImage('test_files/VGA.png', cv.CV_LOAD_IMAGE_GRAYSCALE)
#exit(0)
#cv.Scale(lenaimg, lenaimg, 1);

def test(img):
    print 'Dilate Filter Method'
    out_img = cv.CreateImage(cv.GetSize(img), img.depth, img.nChannels)
    element = cv.CreateStructuringElementEx(7, 7, 0, 0, cv.CV_SHAPE_CROSS)
    t = cv.GetTickCount()
    pyc6accel.Dilate(lenaimg, out_img, element, 1)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "pyc6accel adds detection time = %g ms" % (t / (cv.GetTickFrequency() * 1000.))
    cv.SaveImage('test_files/result_dilate_pyc6accel.png', out_img)
    
#    fd.write(str(msec) + '\t')
#
#    adds_opencv = cv.CreateMat(img.rows, img.cols, cv.CV_8UC1)
#    cv.SetData(adds_pyc6accel, ret, img.width)
#    t = cv.GetTickCount()
#    cv.AddS(img, 100, adds_img)
#    t = cv.GetTickCount() - t
#    msec = t / (cv.GetTickFrequency() * 1000.)
#    print "opencv adds detection time = %g ms" % (t / (cv.GetTickFrequency() * 1000.))
#    cv.SaveImage('test_files/result_adds_opencv.png', adds_img)
#    fd.write(str(msec) + '\t')
    
if __name__ == '__main__' :
    ''''''
    for i in range(1):
        test(lenaimg)