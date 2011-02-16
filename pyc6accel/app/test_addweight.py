import cv
import pyc6accel

lenaimg = cv.LoadImage('test_files/VGA.png', cv.CV_LOAD_IMAGE_GRAYSCALE)
lenaimg_add = cv.LoadImage('test_files/VGA.png', cv.CV_LOAD_IMAGE_GRAYSCALE)
#lenaimg1_16s = cv.CreateImage(cv.GetSize(lenaimg), cv.IPL_DEPTH_16S, lenaimg.nChannels)
#lenaimg2_16s = cv.CreateImage(cv.GetSize(lenaimg), cv.IPL_DEPTH_16S, lenaimg.nChannels)
#cv.Convert(lenaimg, lenaimg1_16s)
#cv.Convert(lenaimg, lenaimg2_16s)
#exit(0)
#cv.Scale(lenaimg, lenaimg, 1);

def test():
    print 'Add Weighted Image Method'
    add_img = cv.CreateImage(cv.GetSize(lenaimg), lenaimg.depth, lenaimg.nChannels)
    t = cv.GetTickCount()
    pyc6accel.AddWeighted(lenaimg, 0.5, lenaimg_add, 0.6, 0, add_img)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "pyc6accel add detection time = %g ms" % (t / (cv.GetTickFrequency() * 1000.))
    cv.SaveImage('test_files/result_add_pyc6accel.png', add_img)
    
#    fd.write(str(msec) + '\t')
#
    adds_opencv = cv.CreateImage(cv.GetSize(lenaimg), lenaimg.depth, lenaimg.nChannels)
#    cv.SetData(adds_pyc6accel, ret, img.width)
    t = cv.GetTickCount()
    cv.AddWeighted(lenaimg, 0.5, lenaimg_add, 0.6, 0, adds_opencv)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "opencv add detection time = %g ms" % (t / (cv.GetTickFrequency() * 1000.))
    cv.SaveImage('test_files/result_add_opencv.png', adds_opencv)
#    fd.write(str(msec) + '\t')
    
if __name__ == '__main__' :
    ''''''
    for i in range(1):
        test()
