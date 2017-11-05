#!/bin/bash
echo "Image Path = $1"
echo "Image Name = $2"
echo "Tag = $3"

cd $1
tag -a $3 $2
