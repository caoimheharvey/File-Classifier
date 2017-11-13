#!/bin/sh

chmod +x face_detection.py
export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH
python face_detection.py $1