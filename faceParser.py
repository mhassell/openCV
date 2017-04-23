""" This is a script for quickly running through test/training sets to make sure the faces are captured correctly """

import os

import cv2
import numpy as np
from PIL import Image

resize = True
if resize:
	dsize = (320,243)

'''Where the pictures are stored'''
directory = 'train'

faceCascadePath = "haarcascade_frontalface_default.xml" 
eyeCascadePath = 'haarcascade_eye.xml'
faceCascade = cv2.CascadeClassifier(faceCascadePath);
eyeCascade = cv2.CascadeClassifier(eyeCascadePath)
recognizer = cv2.createLBPHFaceRecognizer()

image_paths = [os.path.join(directory, f) for f in os.listdir(directory)]

j = 0
for image_path in image_paths:
	print image_path
	if image_path == 'train/.DS_Store':
		continue
	image_pil = Image.open(image_path).convert('L')
	image = np.array(image_pil, 'uint8')
	if resize:
		# cv2.imshow("loaded...",image)
		# cv2.waitKey(0)
		image = cv2.blur(image,(3,3))
		imageResized = cv2.resize(image, dsize, interpolation = cv2.INTER_CUBIC)
		cv2.imwrite('imageGray{}.png'.format(j),imageResized)
		j+=1
	faces = faceCascade.detectMultiScale(image, minNeighbors=3, scaleFactor = 1.2)
	for (x, y, w, h) in faces:
		cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
		cv2.imshow("Verifying face",  image) #image[y: y + h, x: x + w])
		k = cv2.waitKey(0)
		if k == 32: # space
				continue
		elif k == 110: # n
			os.remove(image_path)


cv2.destroyAllWindows()