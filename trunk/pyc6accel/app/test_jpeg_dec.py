import cv
import pyc6accel


def test():
    print 'Decode Image Method'
    fi = open('test_files/lena.jpg', 'rb')

    input = fi.read()
    fi.close()
    t = cv.GetTickCount()
    output = pyc6accel.JpegDecode(input)
    t = cv.GetTickCount() - t
    msec = t / (cv.GetTickFrequency() * 1000.)
    print "pyc6accel jpeg decode detection time = %g ms" % (t / (cv.GetTickFrequency() * 1000.))
    fo = open('test_files/jpeg.yuv', 'wb')
    fo.write(output)
    fo.close()

if __name__ == '__main__' :
    ''''''
    for i in range(1):
        test()
