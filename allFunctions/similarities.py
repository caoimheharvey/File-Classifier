#!/usr/bin/env python
__author__ = "Caoimhe Harvey"

"""
Methods relating to finding the similarities between files
"""

def fileHash(file):
    import hashlib
    BUF_SIZE = 65536
    md5 = hashlib.md5()
    with open(file, 'rb') as f:
        buf = f.read(BUF_SIZE)
        while len(buf) > 0:
            md5.update(buf)
            buf = f.read(BUF_SIZE)
    return md5.hexdigest()

"""
Vector Similarity
Used for larger files
"""
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

def text2Vector(text):
    from collections import Counter
    import re
    WORD = re.compile(r'\w+')
    words = WORD.findall(text)
    return Counter(words)

"""
Comparing two files using Sequence Matcher
"""
def getRatioSmallFiles(file1_path, file2_path):
    from difflib import SequenceMatcher
    file1 = open(file1_path).read()
    file2 = open(file2_path).read()
    similarity = SequenceMatcher(None, file1, file2)
    return similarity.ratio()