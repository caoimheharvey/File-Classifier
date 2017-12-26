#!/usr/bin/env python
__author__ = "Caoimhe Harvey"

"""
Methods for moving files and traversing the directories
"""
def traverse(rootDir):
    import os
    from collections import defaultdict
    import time

    start = time.time()
    imageTable = defaultdict(list)
    list_of_text_files = []

    for dirName, subdirList, fileList in os.walk(rootDir, topdown = False):
        #print('Found directory: %s' % dirName)
        for fname in fileList:
            if (fname.lower().endswith(('.txt'))):
                list_of_text_files.append(dirName + "/" + fname)
            elif (fname.lower().endswith(('.jpg', '.jpeg', '.png'))):
                hashedImage = getHashValue(dirName + "/" + fname)
                imageTable[hashedImage].append(dirName + "/" + fname)
            else:
                continue
        if len(subdirList) > 0:
            del subdirList[0]

    print("LIST OF ALL TEXT FILES", list_of_text_files)
    similar_text_files = mainFileComp(list_of_text_files)
    print("\n\n----------------- DUPLICATES --------------------")
    for key, value in imageTable.items():
        if (len(value) > 1):
            print(key, value)

    for key, value in similar_text_files.items():
        if (len(value) > 1):
            print(key, value)
    print("Total Time: " , time.time() - start)
    print("---------------- PROGRAM ENDED ------------------")

"""
Setting hash value for an image and adding it to a dictionary
"""
def getHashValue(file):
    import hashlib
    BUF_SIZE = 65536
    md5 = hashlib.md5()
    with open(file, 'rb') as f:
        buf = f.read(BUF_SIZE)
        while len(buf) > 0:
            md5.update(buf)
            buf = f.read(BUF_SIZE)
    return md5.hexdigest()



# -----------------------------------------
# All code which is to be executed from the command line goes here
# -----------------------------------------
"""
Running bash commands from python
"""

def runBashCommand(bashCommand):
    import subprocess
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output

def cv2func(image):
    import subprocess
    subprocess.call(["bin/bash", "runCV.sh"], image)

###
###         Code to be replacing anything relating to tags
###

def compare(word, list):
    from difflib import SequenceMatcher
    size = len(list)
    c = 0
    for key, value in list.items():
        if word in list.keys():
            #if word is a key then skip
            return "skip",""
        else:
            #before creating a new key, check if it is similar to already existing keys
            if SequenceMatcher(None, open(word).read(), open(key).read()).ratio() > 0.7:
                return "add", key
            elif c != size:
                continue
            elif c == size:
                return "new", ""
        c += 1
    return "new", ""

def mainFileComp(arr):
    from collections import defaultdict

    dd = defaultdict(list)

    for i in range(len(arr)):
        if(len(dd) == 0):
            dd[arr[i]]
        else:
            r , key = compare(arr[i], dd)
            if r == "add":
                dd[key].append(arr[i])
            elif r == "new":
                dd[arr[i]]
            elif r == "skip":
                continue

    for k , v in dd.items():
        print("key-val", k, v)

    return dd