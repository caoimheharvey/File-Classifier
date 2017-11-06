#!/usr/bin/env python
__author__ = "Caoimhe Harvey"
from functions import FileOperations as fo
from functions import cmdLineFunctions as cmd

file_path = "./text-files/jogabumbum.txt"

frequentWords = fo.commonlyOccurringWords(file_path, 3)

print(frequentWords)

cmd.addFileTag(frequentWords, "./text-files/large1.txt")

cmd.findAllFiles("bum")
