import os
import numpy as np
import cv2
import pickle
from PIL import Image

# Face detection module.
face_cascade = cv2.CascadeClassifier('Cascade/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

Base_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(Base_dir, "images")

current_id = 0
label_id = {}
y_labels = []  # for saving the labels of the image folders.
x_train = []  # for saving the pixel values of the images in the list.

for root, dirs, files in os.walk(image_dir):
	for file in files:
		if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg") or file.endswith("jfif") or file.endswith("JPG"):
			path = os.path.join(root, file)
			label = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower()
			# print(label, path)

			if not label in label_id:
				label_id[label] = current_id
				current_id += 1

			id = label_id[label]
			# print(label_id)
			# y_labels.append(label)  # some number of the image.
			# x_train.append(path)  # verify this image, train into a numpy array.
			pil_image = Image.open(path).convert("L")  # convert to grayscale.
			size = (550, 550)
			final_img = pil_image.resize(size, Image.ANTIALIAS)
			image_arr = np.array(final_img, "uint8")  # converting the image into number form.
			# print(image_arr)
			faces = face_cascade.detectMultiScale(image_arr, scaleFactor=1.2, minNeighbors=6)

			for (x, y, w, h) in faces:
				roi = image_arr[y:y+h, x:x+w]
				x_train.append(roi)
				y_labels.append(id)

# print(y_labels)
# print(x_train)

with open("labels.pickle", 'wb') as f:
	pickle.dump(label_id, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trained.yml")
