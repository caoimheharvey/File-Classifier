#!/usr/bin/env python
__author__ = "Caoimhe Harvey"
"""
Gets Hash Values of similar/equal text files.
Purpose is to determine if hashing is a valid method
to compare text based files for duplication system.
"""
#testing = input("Modifications for this test: ")
from allFunctions import similarities as s

file1_path = input("F1: ")
#file2_path = input("Please enter file path for the second file: ")

print("\nHashing........\n")

hash1 = s.fileHash(file1_path)
print("FILE 1: " + hash1)

"""
testingFile = open("./testingLogs/hashTestingTextFiles.txt", "a")
testingFile.write("\n--------------------------------------------------\n\n")
testingFile.write(testing + "\n")
testingFile.write("\nFile 1: " + file1_path + "\t " + hash1)
testingFile.write("\nFile 2: " + file2_path + "\t " + hash2)
testingFile.write("\n\n--------------------------------------------------\n")
testingFile.close()
"""