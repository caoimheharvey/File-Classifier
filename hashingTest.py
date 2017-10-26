#!/usr/bin/env python 
"""
Gets Hash Values of similar/equal text files.
Purpose is to determine if hashing is a valid method
to compare text based files for duplication system.
"""
__author__ = "Caoimhe Harvey"

testing = input("Modifications for this test: ")
import methods

file1_path = input("Please enter file path for the first file: ")
file2_path = input("Please enter file path for the second file: ")

print("\nHashing........\n")

hash1 = methods.hasht(file1_path)
print("FILE 1: " + hash1)
hash2 = methods.hasht(file2_path)
print("FILE 2: " + hash2)

testingFile = open("./testingLogs/hashTestingTextFiles.txt", "a")
testingFile.write("\n--------------------------------------------------\n\n")
testingFile.write(testing + "\n")
testingFile.write("\nFile 1: " + file1_path + "\t " + hash1)
testingFile.write("\nFile 2: " + file2_path + "\t " + hash2)
testingFile.write("\n\n--------------------------------------------------\n")
testingFile.close()
