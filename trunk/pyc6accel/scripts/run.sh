#!/bin/bash

sudo mv pyc6accel.so /usr/local/lib/python2.6/dist-packages/
sudo mv c6accel_omap3530.x64P /usr/local/lib/python2.6/dist-packages/

# Please comment any lines not used
#python test_rgbtogray.py
#python test_threshold.py
#python test_sobel.py
#python test_adds.py
#python test_subs.py
#python test_add.py	#problem
python test_erode.py
#python test_dilate.py