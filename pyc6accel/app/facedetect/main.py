'''
Created on Jul 23, 2010

@author: anol
'''
import time
import cv, sys
import IPCamera
from optparse import OptionParser
from detect import detect

scale = 1

def main():
	usage = "usage: %prog [options] [<ip_camera>|<local_camera_index>|<video file>]"
	parser = OptionParser(usage)

	parser.add_option("-f", "--filevideo", dest = "vfile", type = "string", help = "Video File Name, default %default", default = None)
	parser.add_option("-i", "--ipaddress", dest = "ipaddr", type = "string", help = "Target IP Address, default %default", default = None)
	parser.add_option("-d", "--device", dest = "device", type = "int", help = "Number of Video Device, default %default", default = None)

	parser.add_option("-c", "--cascade", dest = "cascade", type = "string", help = "Haar Cascade File, default %default", default = "haarcascade_frontalface_default.xml")
	parser.add_option("-o", "--output", dest = "output", type = "string", help = "Output Video File, default %default", default = None)

	(options, args) = parser.parse_args()

	cascade = cv.Load(options.cascade)
	output = options.output

	if options.device != None:
		capture = cv.CreateCameraCapture(options.device)
		camera = None
	elif options.vfile != None:
		capture = cv.CaptureFromFile(options.vfile)
		camera = None
	elif options.ipaddr != None:
		capture = None
		camera = IPCamera.IPCamera('http://%s' % (options.ipaddr), 'half', 1, (0, 0), (1280, 1024))
		camera.openPort()
		camera.start()

	if (camera is None) and (capture is None):
		parser.print_help()
		sys.exit(1)

#	cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 640)
#	cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
	if output == None:
		cv.NamedWindow('test', 2)
	else:
		writer = cv.CreateVideoWriter(output, cv.CV_FOURCC('M', 'J', 'P', 'G'), 10, (320, 240))

	det = detect(cascade)

	while True:
		img = None
		if capture:
			img = cv.QueryFrame(capture)
		else:
			while (camera.getImage() == None):
				cv.WaitKey(100)
			img = camera.getImage()
		small_img = cv.CreateImage((cv.Round(img.width / scale),
               cv.Round (img.height / scale)), 8, 3)
		cv.Resize(img, small_img)
#		img = small_img
		det.detect_and_draw(small_img)
#		img = None
		if output == None:
			cv.ShowImage('test', small_img)
		else:
			cv.WriteFrame(writer, small_img)

		if output == None:
			if cv.WaitKey(10) == 27:
				cv.DestroyAllWindows()
				if camera != None:
					camera.Stop()
				break

#		time.sleep(0.1)
	if camera != None:
		camera.Stop()

if __name__ == '__main__':
	main()
	exit(0)
