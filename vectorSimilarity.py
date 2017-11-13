#!/usr/bin/env python
__author__ = "Caoimhe Harvey"

import time
import functions as m
start = time.time()

text1 = open("./text-files/1.txt").read()
text2 = open("./text-files/large1.txt").read()

vector1 = m.text2Vector(text1)
vector2 = m.text2Vector(text2)

cosine = m.getCosine(vector1, vector2)

print ('Cosine:', cosine * 100)
print ('END TIME: %s' % (time.time() - start))
