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
            if(fname.lower().endswith(('.txt'))):
                continue
            else:
               continue
        if len(subdirList) > 0:
            del subdirList[0]
    print("---------------- DONE ------------------")


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

    print(tags)
    runBashCommand("tag -a " + tags + " " + file_path)
