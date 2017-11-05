#!/usr/bin/env python
import operator

__author__ = "Caoimhe Harvey"

def removePunctuation(word):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in word:
       if char not in punctuations:
           no_punct = no_punct + char
    return no_punct

file_path = "./text-files/jogabumbum.txt"

wordcount = {}
ignore = ['this','a','is',"it", "i", "\n"]

with open(file_path, 'r') as f:
    for line in f:
        for words in line.split():
            word = removePunctuation(words.lower())
            if words not in ignore:
                if word in wordcount:
                    current_count = wordcount[word]
                    wordcount[word] = current_count + 1
                else:
                    wordcount[word.lower()] = 1
            else:
                continue

mostcommon = dict(sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)[:10])

tags = ""
for key,value in mostcommon.items():
    tags += (key + ",")

print(tags)

from functions import FileOperations as fo
fo.addFileTag(tags, "./text-files/small1.txt")

fo.findAllFiles("com")