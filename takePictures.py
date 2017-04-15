# from here: https://codeplasma.com/2012/12/03/getting-webcam-images-with-python-and-opencv-2-for-real-this-time/

import os

from  datetime import date, datetime
import time
import cv2

#file = date.today().isoformat()
file = 'test'
try:
	os.mkdir(file)
except:
	pass

camera_port = 0
ramp_frames = 5
num_pics = 10

camera = cv2.VideoCapture(camera_port)

def get_image():
	retval,im = camera.read()
	if retval:
		return im
	else:
		print 'error capturing image'

# chuck the first few images while the camera adjusts
for i in range(ramp_frames):
	temp=get_image()

print "now taking images"

for i in range(num_pics):
	camera_capture = get_image()
	filename = file + "/image" + str(i) + ".png"
	print filename
	cv2.imwrite(filename, camera_capture) 
	cv2.waitKey(500)

del(camera)