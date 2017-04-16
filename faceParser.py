""" This is a script for quickly running through test/training sets to make sure the faces are captured correctly """

import os

import cv2
import numpy as np
from PIL import Image


'''Where the pictures are stored'''
directory = 'test'

cascadePath = "haarcascade_frontalface_default.xml" 
faceCascade = cv2.CascadeClassifier(cascadePath);
recognizer = cv2.createLBPHFaceRecognizer()

image_paths = [os.path.join(directory, f) for f in os.listdir(directory)]

for image_path in image_paths:
	try:
		image_pil = Image.open(image_path).convert('L')
	except:
		continue
	image = np.array(image_pil, 'uint8')
	faces = faceCascade.detectMultiScale(image)
	for (x, y, w, h) in faces:
		cv2.imshow("Verifying face", image[y: y + h, x: x + w])
		k = cv2.waitKey(0)
		if k == 32: # space
			continue
		elif k == 110: # n
			os.remove(image_path)


cv2.destroyAllWindows()