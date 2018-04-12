#!/usr/bin/env python
# ***********************************************************************
#
#   Functions used in the duplication module of the project.
#
# ***********************************************************************

__author__ = "Caoimhe Harvey"

# ***********************************************************************
#
#   Function: findDuplicates
#
#   Goes through all directories and finds duplicate images and text files.
#       Main part of the duplication finding algorithm. Establishes the files to be compared.
#
#   Parameters:
#       * rootDir: directory to serve as main node. All subdirectories are scanned
#
# ***********************************************************************
def findDuplicates(rootDir):
    import os
    import time

    start = time.time()
    list_of_text_files = []

    for dirName, subdirList, fileList in os.walk(rootDir, topdown = False):
        for fname in fileList:
            if fname.lower().endswith(('.txt', '.docx')):
                list_of_text_files.append(dirName + "/" + fname)
            else:
                continue
        if len(subdirList) > 0:
            del subdirList[0]

    similar_text_files = mainFileComp(list_of_text_files)

    print("\n\n----------------- DUPLICATES --------------------")
    for key, value in similar_text_files.items():
        print("\n",key)
        for v in value:
            print("\t\t",v)

    print("\n\nTotal Time: " , time.time() - start)
    print("---------------- PROGRAM ENDED ------------------")

    return similar_text_files


# ***********************************************************************
#
#   Function: getCosine
#
#   Used to calculate the similarity of two documents through Cosine Similarity.
#
#   Parameters:
#       * vec1: the first of the two files to be compared
#       * vec2: the second of the files to be compared
#
#   Returns:
#       * the vector of similarity
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
#   Function: textToVector
#
#   Converts the text from a document to a mathematical value
#
#   Parameters:
#       * text: string from a document
#
#   Returns:
#       * vector: numerical value associated with the string
#
# ***********************************************************************
def textToVector(text):
    from collections import Counter
    import re
    WORD = re.compile(r'\w+')
    words = WORD.findall(text)
    return Counter(words)


# ***********************************************************************
#
#   Function: checkextension
#
#   Checks the extension of a file and returns it as a string
#
#   Parameters:
#       * file: file of either .docx or .txt
#
#   Returns:
#       * inputted file as a string
#
# ***********************************************************************
def checkextension(file):
    import docx2txt
    if file.lower().endswith('.txt'):
        return open(file, 'r').read()
    else:
        return docx2txt.process(file)

# ***********************************************************************
#
#   Function: Compare
#
#   Function used to compare the existing files in a list to a file and evaluate
#       if they are similar (add as duplicate) or not.
#
#   Parameters:
#       * file: the string of the file itself to be compared
#       * file_path: the path of the file to be compared
#       * list: list of all the existing recognized duplicates
#
#   Returns:
#       * "add", key: add the file as a duplicate to an existing key
#       * "new": does not exist as a key, needs to be created as one
#       * "skip": file path already exists as a key
#
# ***********************************************************************
def compare(file, file_path, list):
    from difflib import SequenceMatcher

    list_len = len(list)
    counter = 0
    for key, value in list.items():
        if file_path in list.keys():
            print("\t\tSKIP\n")
            return "skip",""
        else:
            ratio = SequenceMatcher(None, file, checkextension(key)).ratio()
            if ratio > 0.7:
                print(file_path, "\n\tMATCHES WITH ", key, "\n\tRATIO: ", ratio,"\n" )
                return "add", key
            elif counter != list_len:
                continue

        counter += 1
    return "new", ""


# ***********************************************************************
#
#   Function: MainFileComp
#
#   Heart of the duplication identifier algorithm. Takes in a list of all text based files
#       in a directory and outputs the ones with similar or duplicated content
#
#   Parameters:
#       * arr: array of all text, and docx files to be compared
#
#   Returns:
#       * final: array of all duplicated files
#
# ***********************************************************************
def mainFileComp(paths):
    from collections import defaultdict

    dd = defaultdict(list)
    final = defaultdict(list)

    for i in range(len(paths)):
        if(len(dd) == 0):
            dd[paths[i]]
        else:
            contents = checkextension(paths[i])
            res , key = compare(contents, paths[i], dd)
            if res == "add":
                dd[key].append(paths[i])
            elif res == "new":
                dd[paths[i]]
            elif res == "skip":
                continue
    for k , v in dd.items():
        if dd[k]:
            final[k] = v
    return final