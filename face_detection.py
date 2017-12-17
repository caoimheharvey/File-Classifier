# Caoimhe Harvey
# File deals with uploading and recognizing face in a picture
# !/usr/bin/env python

import cv2
import sys

casc = cv2.CascadeClassifier("face_cascade.xml")

# get image path from command line
imagePath = sys.argv[1]

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# code to detect the faces
faces = casc.detectMultiScale(
    gray,
    scaleFactor=1.01,
    minNeighbors=5,
    minSize=(30, 30),
)

print("Found {0} faces!".format(len(faces)))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Faces Found: ", image)
cv2.waitKey(0)
