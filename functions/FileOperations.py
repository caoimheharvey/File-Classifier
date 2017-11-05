#!/usr/bin/env python
__author__ = "Caoimhe Harvey"

"""
Methods for moving files and traversing the directories

"""
def traverse(rootDir):
    import os
    for dirName, subdirList, fileList in os.walk(rootDir):
        print('Found directory: %s' % dirName)
        for fname in fileList:
            print('\t%s' % fname)
            if(fname.lower().endswith(('.txt','.png', '.jpg', '.jpeg'))):
                continue
            else:
               continue
        if len(subdirList) > 0:
            del subdirList[0]
    print("---------------- DONE ------------------")

def runBashCommand(bashCommand):
    import subprocess
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

def cv2func():
    import subprocess
    command = "export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

