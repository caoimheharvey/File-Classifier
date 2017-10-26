#!/usr/bin/env python 
"""
Gets Hash Values of similar/equal text files.
Purpose is to determine if hashing is a valid method
to compare text based files for duplication system.
"""
__author__ = "Caoimhe Harvey"

input("Modifications for this test: ")
import methods
file1_path = input("Please enter file path for the first file: ")
file2_path = input("Please enter file path for the second file: ")

print("\nHashing........\n")

print("FILE1: {0}" .format(methods.hasht(file1_path)))
print("FILE2: {0}" .format(methods.hasht(file2_path)))
