#!/usr/bin/env python
__author__ = "Caoimhe Harvey"

import cv2

image_path = input("Enter the image path: ")
faceCascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
