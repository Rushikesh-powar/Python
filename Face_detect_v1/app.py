import numpy as np
import pickle
import cv2

# Face detection module.
face_cascade = cv2.CascadeClassifier('Cascade/data/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('Cascade/data/haarcascade_eye.xml')
# smile_cascade = cv2.CascadeClassifier('Cascade/data/haarcascade_smile.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trained.yml")

lables = {"person_name": 1}
with open("labels.pickle", 'rb') as f:
	lables = pickle.load(f)
	lables = {v:k for k, v in lables.items()}

# video capturing frame rate.
cap = cv2.VideoCapture(0)

# This is to change the resolution of the video.
cap.set(3, 1080)
cap.set(4, 720)

while True:
	# Capturing frames.
	ret, frame = cap.read()

	# Converting the color video in grayscale( black and white )
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detecting the face in the frame.
	face = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=6)

	# printing the face dimensions
	for(x, y, w, h) in face:
		# print(x, y, w, h)
		roi_gray = gray[y:y + h, x:x + w]  # The x and y co-ordinates for the frame of the frame.
		roi_color = frame[y:y + h, x:x + w]

		id, conf = recognizer.predict(roi_gray)
		if conf >= 45:  # and conf <= 85:
			print(id)
			print(lables[id])
			font = cv2.FONT_HERSHEY_SIMPLEX
			name = lables[id]
			color = (0, 255, 0)
			stroke = 2
			cv2.putText(frame, name.title(), (x, y), font, 1, color, stroke, cv2.LINE_AA)

		img_item = "my_face.png"  # name of the png img file.

		cv2.imwrite(img_item, roi_color)  # saving the img in the project.

		color = (0, 255, 0)  # BGR value for the blue color, used for the rectangle.

		stroke = 2  # this is to define the thickness of the rectangle.

		end_x_cord = x + w
		end_y_cord = y + h

		# displaying the rectangle of green with starting (x, y) co-ordinates and the ending(x+w, y+h) co_ordinates.
		cv2.rectangle(frame, (x, y), (end_x_cord, end_y_cord), color, stroke)

		# for detecting the eyes of the frame.
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex, ey, ew, eh) in eyes:
			cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

		# for detecting the smile in frame.
		# smile = smile_cascade.detectMultiScale(roi_gray)
		# for (sx, sy, sw, sh) in smile:
		# 	cv2.rectangle(roi_gray, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)

	# Displaying the frame.
	cv2.imshow('Camera', frame)

	# Terminating the video capture.
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
