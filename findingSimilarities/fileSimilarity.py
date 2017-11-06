#!/usr/bin/env python
__author__ = "Caoimhe Harvey"
"""
Designed to retreive the ratio/percentage of how similar two text files are.
Additionally it calculates the time which it takes to compare the two files.

"""
from difflib import SequenceMatcher
import time


testing = input("Modifications for this test: ")
f1 = input("File 1: ")
f2 = input("File 2: ")


start_time = time.time()
text1 = open("./text-files/" + f1 + ".txt").read()
text2 = open("./text-files/" + f2 + ".txt").read()
m = SequenceMatcher(None, text1, text2)
print(m.ratio())
perc = m.ratio() * 100
end_time = time.time() - start_time
print("--- %s seconds ---" % end_time)

testingFile = open("./testingLogs/sequenceMatchTextFiles.txt", "a")
testingFile.write("\n--------------------------------------------------\n\n")
testingFile.write(testing + "\n")
testingFile.write("\nFiles compared: \n")
testingFile.write(f1 + ".txt\t" + f2 + ".txt\n")
testingFile.write("Similarity is at: " + str(perc))
testingFile.write("\n\nTime elapsed: %s" % (time.time() - start_time))
testingFile.write("\n\n--------------------------------------------------\n")
testingFile.close()
