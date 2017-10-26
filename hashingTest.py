#!/usr/bin/env python 
"""
Gets Hash Values of similar/equal text files.
Purpose is to determine if hashing is a valid method
to compare text based files for duplication system.
"""
__author__ = "Caoimhe Harvey"

import hashlib

def hash(file):
    BUF_SIZE = 65536
    md5 = hashlib.md5()

    with open(file1_path, 'rb') as file:
        buf = file.read(BUF_SIZE)
        while len(buf) > 0:
            md5.update(buf)
            buf = file.read(BUF_SIZE)
    return md5.hexdigest()

file1_path = input("Please enter file path for the first file: ")
file2_path = input("Please enter file path for the second file: ")

print("\n\nHashing........\n\n")

print("File1 HASH: {0}" .format(hash(file1_path)))
print("File2 HASH: {0}" .format(hash(file2_path)))
