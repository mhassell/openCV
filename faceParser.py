""" This is a script for quickly running through test/training sets to make sure the faces are captured correctly """

import os

import cv2
import numpy as np
from PIL import Image

resize = False

if resize:
	dsize = (500,500)

'''Where the pictures are stored'''
directory = 'train'

faceCascadePath = "haarcascade_frontalface_default.xml" 
eyeCascadePath = 'haarcascade_eye.xml'
faceCascade = cv2.CascadeClassifier(faceCascadePath);
eyeCascade = cv2.CascadeClassifier(eyeCascadePath)
recognizer = cv2.createLBPHFaceRecognizer()

image_paths = [os.path.join(directory, f) for f in os.listdir(directory)]

for image_path in image_paths:
	if image_path == 'train/.DS_Store':
		continue
	image_pil = Image.open(image_path).convert('L')
	image = np.array(image_pil, 'uint8')
	if resize:
		print(image.shape)
		image = cv2.resize(image, dsize, interpolation = cv2.INTER_CUBIC)
		cv2.imshow("resized image", image)
	faces = faceCascade.detectMultiScale(image, minNeighbors=3, scaleFactor = 1.2)
	eyes = eyeCascade.detectMultiScale(image, minNeighbors=5, scaleFactor = 1.2)
	for (x, y, w, h) in faces:
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(image,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
		cv2.imshow("Verifying face",  image) #image[y: y + h, x: x + w])
		k = cv2.waitKey(0)
		if k == 32: # space
			continue
		elif k == 110: # n
			os.remove(image_path)


cv2.destroyAllWindows()