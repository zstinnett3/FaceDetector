#!/usr/bin/env python
# coding: utf-8

# method name: Face Counter
# purpose: This script counts the number of faces in your webcam's view
# created: 12/124/2020 5:01PM
# Author: Zack Stinnett
# Sources: https://www.geeksforgeeks.org/count-number-of-faces-using-python-opencv/
# Revisions: 

#%pip install opencv-python
#%pip install cmake
#%pip install https://pypi.python.org/packages/da/06/bd3e241c4eb0a662914b3b4875fc52dd176a9db0d4a2c915ac2ad8800e9e/dlib-19.7.0-cp36-cp36m-win_amd64.whl#md5=b7330a5b2d46420343fbed5df69e6a3f



# Import required libraries 
import cv2 
import numpy as np 
import dlib 


# Connects to your computer's default camera 
cap = cv2.VideoCapture(0) 


# Detect the coordinates 
detector = dlib.get_frontal_face_detector() 


# Capture frames continuously 
while True: 

	# Capture frame-by-frame 
	ret, frame = cap.read() 
	frame = cv2.flip(frame, 1) 

	# RGB to grayscale 
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
	faces = detector(gray) 

	# Iterator to count faces 
	i = 0
	for face in faces: 

		# Get the coordinates of faces 
		x, y = face.left(), face.top() 
		x1, y1 = face.right(), face.bottom() 
		cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2) 

		# Increment iterator for each face in faces 
		i = i+1

		# Display the box and faces 
		cv2.putText(frame, 'face num'+str(i), (x-10, y-10), 
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2) 
		print(face, i) 

	# Display the resulting frame 
	cv2.imshow('frame', frame) 

	# This command let's us quit with the "q" button on a keyboard. 
	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break


# Release the capture and destroy the windows 
cap.release() 
cv2.destroyAllWindows() 
