import cv
import pyc6accel
from numpy.numarray import random_array


#lenaimg = cv.LoadImageM('test_files/road_grey.pgm', cv.CV_LOAD_IMAGE_GRAYSCALE)
lenaimg = cv.LoadImage('test_files/lena.jpg', cv.CV_LOAD_IMAGE_GRAYSCALE)
cv.Scale(lenaimg, lenaimg, 1);
#lenaimg = cv.LoadImageM('test_files/scarlett-johansson-pic-4.jpg', cv.CV_LOAD_IMAGE_COLOR)

fd = open("test_files/result.txt", "w+")
fd.write("element\tresolution\ttime\tpyc6accel\topencv\n")
display = [ {"VGA" : (640, 480)} \
          , {"SVGA" : (800, 600)} \
          , {"XGA" : (1024, 768)} \
          , {"XGA+" : (1152, 864)} \
          , {"WXGA" : (1280, 800)} \
          , {"SXGA" : (1280, 960)} \
          , {"HD" : (1366, 768)} \
          , {"WSXGA" : (1440, 900)} \
          , {"HD+" : (1600, 900)} \
#          , {"UXGA" : (1600, 1200)} \
#          , {"WSXGA+" : (1680, 1050)} \
#          , {"HD-1080" : (1920, 1080)} \
#          , {"WUXGA" : (1920, 1200)} \
          ]
#def canny(img, cv, img_data):
#    print 'Canny Method'
#    pyc6accel.init(len(img_data))
#    t = cv.GetTickCount()
#    ret = pyc6accel.canny(img_data, img.rows, img.cols, 1, 10, 3)
#    t = cv.GetTickCount() - t
#    print "pyc6accel canny detection time = %gms" % (t / (cv.GetTickFrequency() * 1000.))
#    pyc6accel.exit()
#    canny_pyc6accel = cv.CreateMatHeader(img.rows, img.cols, cv.CV_8UC1)
#    cv.SetData(canny_pyc6accel, ret, img.width)
#    cv.SaveImage('test_files/road_grey_canny_pyc6accel.pgm', canny_pyc6accel)
#
def sobel(img):
    print 'Sobel Method'
    sobel_pyc6accel = cv.CreateImage(cv.GetSize(img), img.depth, img.nChannels)
    t = cv.GetTickCount()
    ret = pyc6accel.Sobel(img, sobel_pyc6accel, 3)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "pyc6accel sobel detection time = %gms" % (t / (cv.GetTickFrequency() * 1000.))
    fd.write(str(msec) + '\t')

    sobel_opencv_16 = cv.CreateImage(cv.GetSize(img), cv.IPL_DEPTH_16S, img.nChannels)
    sobel_opencv_8 = cv.CreateImage(cv.GetSize(img), img.depth, img.nChannels)
    cv.SaveImage('test_files/result_sobel_pyc6accel.jpg', sobel_pyc6accel)
    t = cv.GetTickCount()
    cv.Sobel(img, sobel_opencv_16, 1, 1, 3)
    cv.ConvertScaleAbs(sobel_opencv_16, sobel_opencv_8, 1, 0)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "opencv sobel detection time = %gms" % (t / (cv.GetTickFrequency() * 1000.))
    cv.SaveImage('test_files/result_sobel_opencv.jpg', sobel_opencv_8)
    fd.write(str(msec) + '\t')
#
def adds(img):
    print 'Add Method'
#    pyc6accel.init(img_data.__sizeof__())
##    pyc6accel.setBuff(img_data)
    adds_img = cv.CreateImage(cv.GetSize(img), img.depth, img.nChannels)
    t = cv.GetTickCount()
    pyc6accel.AddS(img, 100, adds_img)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "pyc6accel adds detection time = %g ms" % (t / (cv.GetTickFrequency() * 1000.))
#    pyc6accel.exit()
    fd.write(str(msec) + '\t')
#
#    adds_opencv = cv.CreateMat(img.rows, img.cols, cv.CV_8UC1)
#    cv.SetData(adds_pyc6accel, ret, img.width)
    cv.SaveImage('test_files/result_adds_pyc6accel.jpg', adds_img)
    t = cv.GetTickCount()
    cv.AddS(img, 100, adds_img)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "opencv adds detection time = %g ms" % (t / (cv.GetTickFrequency() * 1000.))
    cv.SaveImage('test_files/result_adds_opencv.jpg', adds_img)
    fd.write(str(msec) + '\t')
def subs(img):
    print 'SubS Method'
#    pyc6accel.init(img_data.__sizeof__())
##    pyc6accel.setBuff(img_data)
    adds_img = cv.CreateImage(cv.GetSize(img), img.depth, img.nChannels)
    t = cv.GetTickCount()
    pyc6accel.SubS(img, 100, adds_img)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "pyc6accel subs detection time = %g ms" % (t / (cv.GetTickFrequency() * 1000.))
#    pyc6accel.exit()
    fd.write(str(msec) + '\t')
#
#    adds_opencv = cv.CreateMat(img.rows, img.cols, cv.CV_8UC1)
#    cv.SetData(adds_pyc6accel, ret, img.width)
    cv.SaveImage('test_files/result_subs_pyc6accel.jpg', adds_img)
    t = cv.GetTickCount()
    cv.AddS(img, 100, adds_img)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "opencv subs detection time = %g ms" % (t / (cv.GetTickFrequency() * 1000.))
    cv.SaveImage('test_files/result_subs_opencv.jpg', adds_img)
    fd.write(str(msec) + '\t')
def convertcolor(img):
    print 'RGB to Gray Method'
    outrgb2y = cv.CreateImage(cv.GetSize(img), img.depth, 1)
    t = cv.GetTickCount()
    pyc6accel.CvtColor(img, outrgb2y, cv.CV_RGB2GRAY)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "pyc6accel rgb2g detection time = %g ms" % msec
    fd.write(str(msec) + '\t')
    cv.SaveImage('test_files/result_rgb2g_pyc6accel.jpg', outrgb2y)
    t = cv.GetTickCount()
    cv.CvtColor(img, outrgb2y, cv.CV_RGB2GRAY)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "opencv rgb2g detection time = %g ms" % msec
    cv.SaveImage('test_files/result_rgb2g_opencv.jpg', outrgb2y)
    fd.write(str(msec) + '\t')

#def thr_gt2max(img, cv, img_data):
#    print 'Threshold gt 2 max Method'
#    pyc6accel.init(img_data.__sizeof__())
#    t = cv.GetTickCount()
#    ret = pyc6accel.gt2max_8(img_data, img.rows, img.cols, 200)
#    t = cv.GetTickCount() - t
#    msec = t / (cv.GetTickFrequency() * 1000.)
#    print "pyc6accel gt2max detection time = %gms" % (t / (cv.GetTickFrequency() * 1000.))
#    fd.write(str(msec) + '\t')
#    pyc6accel.exit()
#    gt2max_opencv = cv.CreateMat(img.rows, img.cols, cv.CV_8UC1)
#    gt2max_pyc6accel = cv.CreateMatHeader(img.rows, img.cols, cv.CV_8UC1)
#    cv.SetData(gt2max_pyc6accel, ret, img.width)
#    cv.SaveImage('test_files/lena_pyc6accel_gt2max_pyc6accel.jpg', gt2max_pyc6accel)
#    t = cv.GetTickCount()
#    cv.Threshold(img, gt2max_opencv, 100, 255, cv.CV_THRESH_BINARY)
#    t = cv.GetTickCount() - t
#    msec = t / (cv.GetTickFrequency() * 1000.)
#    fd.write(str(msec) + '\t')
#    print "opencv gt2max detection time = %gms" % (t / (cv.GetTickFrequency() * 1000.))
#    cv.SaveImage('test_files/lena_pyc6accel_gt2ma_opencv.jpg', gt2max_opencv)
#
#
#def median_3x3_8(img, cv, img_data):
#    print 'Median Method'
#    pyc6accel.init(img_data.__sizeof__())
#    t = cv.GetTickCount()
#    ret = pyc6accel.median_3x3_8(img_data, img.width)
#    t = cv.GetTickCount() - t
#    msec = t / (cv.GetTickFrequency() * 1000.)
##    print "pyc6accel gt2max detection time = %gms" % (t / (cv.GetTickFrequency() * 1000.))
#    fd.write(str(msec) + '\t')
#    pyc6accel.exit()
#    median_opencv = cv.CreateMat(img.rows, img.cols, cv.CV_8UC1)
##    gt2max_pyc6accel = cv.CreateImageHeader(cv.GetSize(img), cv.IPL_DEPTH_8U, 1)
##    cv.SetData(gt2max_pyc6accel, ret, img.width)
##    cv.SaveImage('test_files/lena_pyc6accel_gt2max_pyc6accel.jpg', gt2max_pyc6accel)
#    t = cv.GetTickCount()
#    cv.Smooth(img, median_opencv, cv.CV_MEDIAN, 3, 3)
#    t = cv.GetTickCount() - t
#    msec = t / (cv.GetTickFrequency() * 1000.)
#    fd.write(str(msec) + '\t')
#
#def histogram_8(img, cv, img_data):
#    print 'Histogram 8 Method'
#    pyc6accel.init(img_data.__sizeof__())
#    t = cv.GetTickCount()
#    ret = pyc6accel.histogram_8(img_data)
#    t = cv.GetTickCount() - t
#    msec = t / (cv.GetTickFrequency() * 1000.)
##    print "pyc6accel gt2max detection time = %gms" % (t / (cv.GetTickFrequency() * 1000.))
#    fd.write(str(msec) + '\t')
#    pyc6accel.exit()
#    median_opencv = cv.CreateMat(img.rows, img.cols, cv.CV_8UC1)
##    gt2max_pyc6accel = cv.CreateImageHeader(cv.GetSize(img), cv.IPL_DEPTH_8U, 1)
##    cv.SetData(gt2max_pyc6accel, ret, img.width)
##    cv.SaveImage('test_files/lena_pyc6accel_gt2max_pyc6accel.jpg', gt2max_pyc6accel)
#    t = cv.GetTickCount()
#    cv.HSmooth(img, median_opencv, cv.CV_MEDIAN, 3, 3)
#    t = cv.GetTickCount() - t
#    msec = t / (cv.GetTickFrequency() * 1000.)
#    fd.write(str(msec) + '\t')
def threshold(img, value):
    ''''''
    print 'Threshold Method'
    out_pyc6accel = cv.CreateImage(cv.GetSize(img), img.depth, img.nChannels)
    t = cv.GetTickCount()
    pyc6accel.Threshold(img, out_pyc6accel, value, pyc6accel.THRESH_LESS2THRES)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "pyc6accel Threshold detection time = %g ms" % msec
    fd.write(str(msec) + '\t')
    cv.SaveImage('test_files/result_Threshold_pyc6accel.jpg', out_pyc6accel)

    out_opencv = cv.CreateImage(cv.GetSize(img), img.depth, img.nChannels)
    t = cv.GetTickCount()
    cv.Threshold(img, out_opencv, value, 255, cv.CV_THRESH_TOZERO_INV)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "opencv Threshold detection time = %g ms" % msec
    cv.SaveImage('test_files/result_Threshold_opencv.jpg', out_opencv)
    fd.write(str(msec) + '\t')

def generate_dataset(width, height, depth):
#    dat = random_array.random_integers(255, 0, [height, width, depth])and 
    dat = random_array.random([height, width, depth])
    return dat

def load(img):
    ''''''
    gray = cv.CreateImage(cv.GetSize(img), 8, 1)
#    ret = pyc6accel.load(gray)
#    pyc6accel.init()
    ret = pyc6accel.RGB2Gray(img, gray)
#    ret = pyc6accel.rgb2y(img.tostring(), img.height, img.width)
    print 'Finish'
    cv.SaveImage('test_files/lena_pyc6accel_RGB2Gray.jpg', gray)

def main():


    for resolute in display:
        name, resolution = resolute.items()[0]
        width = resolution[0]
        height = resolution[1]
        element = width * height
        print name + " : " + resolution.__str__() + " resolution\n"
        fd.write(name + "\t" + resolution.__str__() + '\t' + str(element) + '\t')
#        mat = cv.fromarray(dataset(width, height, 3))
#        dst = cv.CreateImageHeader((width, height), 8, 1)
#        cv.SetData(dst, generate_dataset(width, height, 1))
#        cv.Convert(mat, dst)

#        dst = cv.CreateMat(lenaimg.rows, lenaimg.cols, cv.CV_8UC3)
#        cv.Convert(lenaimg, dst)
#        sobel(lenaimg)
#        adds(lenaimg)
#        subs(lenaimg)
#        convertcolor(lenaimg)
        threshold(lenaimg, 100)
#        load(lenaimg)

        fd.write('\n')
        fd.flush()
#        break

    fd.close()


#    img_data = scarimg.tostring()
#    img_data = lenaimg.tostring()
#    img_data = img.tostring()
#    sobel_test(img, cv, img_data)
#    add_test(img, cv, img_data)
#    canny(img, cv, img_data)
#conversion
#    print len(img_data)
#    cv.NamedWindow("Lena", 1)
#    cv.NamedWindow("Edge", 1)
#    cv.NamedWindow("bar", 1)
#    cv.CreateTrackbar("Thr1", "bar", 0, 1000, onChangeThr1)
#    cv.CreateTrackbar("Thr2", "bar", 0, 1000, onChangeThr2)
#    while True:
#
#        if cv.WaitKey() == "q" :
#            break
#    thr_gt2max(lenaimg, cv, img_data)
#    rgb2y(lenaimg, cv, img_data)

def testadd(img, input, output):
    print 'Test Add Method'
    t = cv.GetTickCount()
    ret = pyc6accel.adds_8(input, output, 50)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "pyc6accel adds detection time = %gms" % (t / (cv.GetTickFrequency() * 1000.))
#    pyc6accel.exit()
    fd.write(str(msec) + '\t')

    adds_pyc6accel = cv.CreateMatHeader(img.rows, img.cols, cv.CV_8UC1)
    cv.SetData(adds_pyc6accel, ret.buffer , img.width)
    cv.SaveImage('test_files/road_grey_pyc6accel_adds_pyc6accel.pgm', adds_pyc6accel)

    adds_opencv = cv.CreateMat(img.rows, img.cols, cv.CV_8UC1)
    t = cv.GetTickCount()
    cv.AddS(img, 100, adds_opencv)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "opencv adds detection time = %gms" % (t / (cv.GetTickFrequency() * 1000.))
    cv.SaveImage('test_files/road_grey_pyc6accel_adds_opencv.pgm', adds_opencv)
    fd.write(str(msec) + '\t')

if __name__ == '__main__':

#    pyc6accel.init()
    main()
#    input = pyc6accel.Buffer()
#    output = pyc6accel.Buffer()
#    data = lenaimg.tostring()
#    status = input.__init__(data, data. __sizeof__())
#    status = output.__init__('', data. __sizeof__())
#    testadd(lenaimg, input, output)
#    fd.write('\n')
#    fd.close()


