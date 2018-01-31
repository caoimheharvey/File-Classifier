#!/usr/bin/env python

###
###                 This file contains all functions for the duplicate file finder module
###
###
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
        for fname in fileList:
            if fname.lower().endswith(('.txt')):
                list_of_text_files.append(dirName + "/" + fname)
            elif fname.lower().endswith(('.jpg', '.jpeg', '.png')):
                hashedImage = getHashValue(dirName + "/" + fname)
                imageTable[hashedImage].append(dirName + "/" + fname)
            else:
                continue
        if len(subdirList) > 0:
            del subdirList[0]

    similar_text_files = mainFileComp(list_of_text_files)

    print("\n\n----------------- DUPLICATES --------------------")
    print("\n\t\t-------- Images --------")
    for key, value in imageTable.items():
        if len(value) > 1:
            print(key, value)

    print("\n\t\t------ Text Files ------")
    for key, value in similar_text_files.items():
        print(key, value)
    print("\n\nTotal Time: " , time.time() - start)
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


"""
Vector Similarity
Used for larger files
"""
def getCosine(vec1, vec2):
    import math
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text2Vector(text):
    from collections import Counter
    import re
    WORD = re.compile(r'\w+')
    words = WORD.findall(text)
    return Counter(words)


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
###         FINDING SIMILAR TEXT FILES
###

def compare(word, list):
    from difflib import SequenceMatcher
    list_len = len(list)
    counter = 0
    for key, value in list.items():
        if word in list.keys():
            #if word is a key then skip
            return "skip",""
        else:
            #before creating a new key, check if it is similar to already existing keys
            if SequenceMatcher(None, open(word).read(), open(key).read()).ratio() > 0.7:
                return "add", key
            elif counter != list_len:
                continue
            elif counter == list_len:
                return "new", ""

        counter += 1
    return "new", ""

def mainFileComp(arr):
    from collections import defaultdict

    dd = defaultdict(list)
    final = defaultdict(list)

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
        if dd[k]:
            final[k] = v

    return final