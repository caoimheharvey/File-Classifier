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
    print(output)

def cv2func():
    import subprocess
    command = "export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

"""
Adding a tag to a file or folder --- used to help identify the contents
"""
def addFileTag(tags, file_path):
    """import subprocess
    output = subprocess.check_output(['./scripts/tagging.sh', tags, file_path])
    print(output)"""
    runBashCommand("tag -a " + tags + " " + file_path)

"""
searching current directory for all files/directories with a certain tag
"""
def findAllFiles(tags):
    runBashCommand("tag -f " + tags)