import os

import cv2
import numpy as np
from PIL import Image

""" User input here """

resize = True # flag to standardize the image size
train_directory = "train"
test_directory = "test"
cascadePath = "haarcascade_frontalface_default.xml" 
if resize:
	dsize = (500,500)

"""Everything from here is autopilot."""

faceCascade = cv2.CascadeClassifier(cascadePath);
recognizer = cv2.createLBPHFaceRecognizer()

# training happens here
def get_images(directory):
	image_paths = [os.path.join(directory, f) for f in os.listdir(directory)]
	images = []
	labels = []
	for image_path in image_paths:
		if image_path == 'train/.DS_Store':
			continue
		image_pil = Image.open(image_path).convert('L')
		image = np.array(image_pil, 'uint8')
		if resize:
			image = cv2.resize(image, dsize, interpolation = cv2.INTER_CUBIC)
			image = cv2.medianBlur(image,5)
			#image = cv2.blur(image,(8,8))
		if image_path[0:11] == 'train/image':
			nbr = 1
		else:
			nbr = 0
		faces = faceCascade.detectMultiScale(image)
		for (x, y, w, h) in faces:
			images.append(image[y: y + h, x: x + w])
			labels.append(nbr)
			cv2.imshow("Adding faces to training set...", image[y: y + h, x: x + w])
			cv2.waitKey(50)
	return images, labels

images, labels = get_images(train_directory)
cv2.destroyAllWindows()
recognizer.train(images, np.array(labels))

# testing happens here

image_paths = [os.path.join(test_directory, f) for f in os.listdir(test_directory)]

for image_path in image_paths:
	if image_path != 'test/.DS_Store':
		predict_image_pil = Image.open(image_path).convert('L')
		predict_image = np.array(predict_image_pil, 'uint8')
		faces = faceCascade.detectMultiScale(predict_image)
		if image_path[0:10]=="test/image":		
			nbr_actual = 1
		else:
			nbr_actual = 0
		for (x, y, w, h) in faces:
			nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
			if nbr_actual == nbr_predicted:
				print "{} is Correctly Recognized with confidence {}".format(nbr_actual, conf)
			else:
				print "{} is Incorrectly Recognized as {}".format(nbr_actual, nbr_predicted)

			cv2.imshow("Recognizing Face", predict_image[y: y + h, x: x + w])
			cv2.waitKey(1000)