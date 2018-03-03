#!/usr/bin/env python


__author__ = "Caoimhe Harvey"

# ***********************************************************************
#
#   Function: Traverse
#
#   Goes through all directories and finds duplicate images and text files.
#       Main part of the duplication finding algorithm. Establishes the files to be compared.
#
#   Parameters:
#       * rootDir: directory to serve as main node. All subdirectories are scanned
#
# ***********************************************************************
def traverse(rootDir):
    import os
    from collections import defaultdict
    import time

    start = time.time()
    imageTable = defaultdict(list)
    list_of_text_files = []

    for dirName, subdirList, fileList in os.walk(rootDir, topdown = False):
        for fname in fileList:
            if fname.lower().endswith(('.txt', '.docx')):
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

# ***********************************************************************
#
#   Function: getHashValue
#
#   Generates the hash value of a file
#
#
#   Parameters:
#       * file: file from which a hash value will be generated
#
#   Returns:
#       * hash value
#
# ***********************************************************************
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


# ***********************************************************************
#
#   Function: getCosine
#
#
#
#
#   Parameters:
#       * vec1:
#       * vec2:
#
# ***********************************************************************
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

# ***********************************************************************
#
#   Function: text2Vector
#
#   Converts the
#
#
#   Parameters:
#       * text
#
# ***********************************************************************
def text2Vector(text):
    from collections import Counter
    import re
    WORD = re.compile(r'\w+')
    words = WORD.findall(text)
    return Counter(words)



# ***********************************************************************
#
#   Function: RunBashCommand
#
#   Function used to run a command from bash
#
#
#   Parameters:
#       * bashCommand: command desired to run
#
# ***********************************************************************

def runBashCommand(bashCommand):
    import subprocess
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output

# ***********************************************************************
#
#   Function: Compare
#
#   Function used to compare the existing files in a list to a file and evaluate
#       if they are similar (add as duplicate) or not.
#
#
#   Parameters:
#       * file: the string of the file itself to be compared
#       * file_path: the path of the file to be compared
#       * list: list of all the existing recognized duplicates
#
# ***********************************************************************
def compare(file, file_path, list):
    from difflib import SequenceMatcher

    list_len = len(list)
    counter = 0
    for key, value in list.items():
        if file_path in list.keys():
            return "skip",""
        else:

            if SequenceMatcher(None, file,
                               open(key).read()).ratio() > 0.7:
                return "add", key
            elif counter != list_len:
                continue
            elif counter == list_len:
                return "new", ""

        counter += 1
    return "new", ""


# ***********************************************************************
#
#           TODO: Add comparison factor for docx files to text files
#   Function: MainFileComp
#
#   Heart of the duplication identifier algorithm. Takes in a list of all text based files
#       in a directory and outputs the ones with similar or duplicated content
#
#   Parameters:
#       * arr: array of all text, and docx files to be compared
#
# ***********************************************************************
def mainFileComp(arr):
    from collections import defaultdict

    dd = defaultdict(list)
    final = defaultdict(list)

    for i in range(len(arr)):
        if(len(dd) == 0):
            dd[arr[i]]
        else:
            res , key = compare(open(arr[i], 'rb').read(),arr[i], dd)
            if res == "add":
                dd[key].append(arr[i])
            elif res == "new":
                dd[arr[i]]
            elif res == "skip":
                continue
    for k , v in dd.items():
        if dd[k]:
            final[k] = v

    return final