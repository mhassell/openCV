# script to organize the test and training sets

import os

train_directory = "train"
test_directory = "test"

# set up the training images
image_paths = [os.path.join(train_directory, f) for f in os.listdir(train_directory)]
j = 0
for image in image_paths:
	if image[0:11] == "train/image":  # pictures I took for training
		pass
	else:						# from the yale library
		os.rename(image, 'train/notme' + str(j) + '.png')
		j+=1

# set up the testing images
image_paths = [os.path.join(test_directory, f) for f in os.listdir(test_directory)]
j = 0
for image in image_paths:
	if image[0:10] == "test/image":  # pictures I took for testing
		pass
	else:						# from the googles
		os.rename(image, 'test/notme' + str(j) + '.png')
		j+=1