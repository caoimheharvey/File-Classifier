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
    for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
        #print('Found directory: %s' % dirName)
        for fname in fileList:
            if (fname.lower().endswith(('.txt'))):
                setTags(dirName + "/" + fname, 4)
            elif (fname.lower().endswith(('.jpg', '.jpeg', '.png'))):
                hashedImage = getHashValue(dirName + "/" + fname)
                imageTable[hashedImage].append(dirName + "/" + fname)
            else:
                continue
        if len(subdirList) > 0:
            del subdirList[0]
    for key, value in imageTable.items():
        if (len(value) > 1):
            print(key, value)
    print("Total Time: " , time.time() - start)
    print("---------------- DONE ------------------")

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
Removes punctuation from a word
"""
def removePunctuation(word):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in word:
       if char not in punctuations:
           no_punct = no_punct + char
    return no_punct

"""
Gets the commonly occuring words from a text
and returns them as a tag to the user
"""
def setTags(file, numberOfTags):
    import operator
    wordcount = {}
    #to be read in from a file
    ignore = ["i", "this", "is", "it", "am", "as", "    ", "\t"]
    with open(file, 'rb') as f:
        for line in f:
            for words in line.split():
                word = removePunctuation(str(words.lower()))
                if words not in ignore:
                    if word in wordcount:
                        current_count = wordcount[word]
                        wordcount[word] = current_count + 1
                    else:
                        wordcount[word.lower()] = 1
                else:
                    continue

    mostcommon = dict(sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)[:numberOfTags])

    tags = ""
    for key, value in mostcommon.items():
        tags += (key[1:] + ",")

    runBashCommand("tag -a " + tags + " " + file)

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

def cv2func():
    import subprocess
    command = "export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

"""
searching current directory for all files/directories with a certain tag
"""
def findAllFiles(tags):
    r = runBashCommand("tag -f " + tags)
    return str(r)[2:-3].split("\\n")


"""
get similarity ratio
"""

def simRatio(file1, file2):
    from difflib import SequenceMatcher
    s = SequenceMatcher(None, open(file1).read(), open(file2).read())
    return s.ratio()

"""
check for repetition
"""
def checkRep(key, value, arr):
    temp = value
    print("key ", arr[key])
    print("val ", arr[value])
    if (key in arr) and (value in arr):
        print("exists")
    else:
        print("new")