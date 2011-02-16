'''
Created on Jul 23, 2010

@author: anol
'''
import time
import cv, sys
import IPCamera
from optparse import OptionParser
from detect import detect


def main():
	usage = "usage: %prog [options] [ip_camera|local_camera_index]"
	parser = OptionParser(usage)

	parser.add_option("-c", "--cascade", dest = "cascade", type = "string", help = "Haar cascade file, default %default", default = "./haarcascade_frontalface_alt2.xml")
	parser.add_option("-o", "--output", dest = "output", type = "string", help = "output file, default %default")
	(options, args) = parser.parse_args()

	cascade = cv.Load(options.cascade)
	output = options.output

	if len(args) != 1:
		parser.print_help()
		sys.exit(1)

	input_name = args[0]
	if input_name.isdigit():
		capture = cv.CreateCameraCapture(int(input_name))
		camera = None
	elif input_name.find('.flv') > 0:
		capture = cv.CaptureFromFile(input_name)
	else:
		capture = None
		camera = IPCamera.IPCamera()
#		camera.scan_ip_network(args[0])
#		camera.createCapture()
		camera.Start()
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
			small_img = cv.CreateImage((cv.Round(img.width / 1.5),
                   cv.Round (img.height / 1.5)), 8, 3)
			cv.Resize(img, small_img)
			img = small_img
		else:
#			img = camera.getImage()
			img = camera.NextFrame()

#		det.detect_object(img)
		det.detect_and_draw(img)

		if output == None:
			cv.ShowImage('test', img)
		else:
			cv.WriteFrame(writer, img)

		if output == None:
			if cv.WaitKey(10) >= 0:
				cv.DestroyAllWindows()
				if camera != None:
					camera.closeCapture()
				break

		time.sleep(0.1)

if __name__ == '__main__':
	main()
	exit(0)
