import cv
import pyc6accel

lenaimg = cv.LoadImage('test_files/lena.jpg', cv.CV_LOAD_IMAGE_GRAYSCALE)
lenaimg1_16s = cv.CreateImage(cv.GetSize(lenaimg), cv.IPL_DEPTH_16S, lenaimg.nChannels)
lenaimg2_16s = cv.CreateImage(cv.GetSize(lenaimg), cv.IPL_DEPTH_16S, lenaimg.nChannels)
cv.Convert(lenaimg, lenaimg1_16s)
cv.Convert(lenaimg, lenaimg2_16s)
#exit(0)
#cv.Scale(lenaimg, lenaimg, 1);

def test():
    print 'Add Image Method'
    add_img = cv.CreateImage(cv.GetSize(lenaimg1_16s), lenaimg1_16s.depth, lenaimg1_16s.nChannels)
    t = cv.GetTickCount()
    pyc6accel.Add(lenaimg1_16s, lenaimg2_16s, add_img)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "pyc6accel adds detection time = %g ms" % (t / (cv.GetTickFrequency() * 1000.))
    cv.SaveImage('test_files/result_add_pyc6accel.jpg', add_img)
    
#    fd.write(str(msec) + '\t')
#
#    adds_opencv = cv.CreateMat(img.rows, img.cols, cv.CV_8UC1)
#    cv.SetData(adds_pyc6accel, ret, img.width)
#    t = cv.GetTickCount()
#    cv.AddS(img, 100, adds_img)
#    t = cv.GetTickCount() - t
#    msec = t / (cv.GetTickFrequency() * 1000.)
#    print "opencv adds detection time = %g ms" % (t / (cv.GetTickFrequency() * 1000.))
#    cv.SaveImage('test_files/result_adds_opencv.jpg', adds_img)
#    fd.write(str(msec) + '\t')
    
if __name__ == '__main__' :
    ''''''
    for i in range(1):
        test()
