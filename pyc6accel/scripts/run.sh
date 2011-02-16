#!/bin/bash

#sudo chmod 777 pyc6accel.so
#sudo chmod 777 c6accel_omap3530.x64P

#sudo cp pyc6accel.so /usr/local/lib/python2.6/dist-packages/
#sudo cp c6accel_omap3530.x64P /usr/local/lib/python2.6/dist-packages/

# Please comment any lines not used
python test_rgbtogray.py
#python test_threshold.py
#python test_sobel.py
python test_adds.py
#python test_subs.py
python test_add.py
#python test_erode.py
#python test_dilate.py
#python test_muls.py
#python test_addweight.py

#test face detection
#python facedetect/main.py 0
