#!/usr/bin/env python
__author__ = "Caoimhe Harvey"

import time
import methods as m
start = time.time()

text1 = open("./text-files/1.txt").read()
text2 = open("./text-files/large1.txt").read()

vector1 = m.text_to_vector(text1)
vector2 = m.text_to_vector(text2)

cosine = m.get_cosine(vector1, vector2)

print ('Cosine:', cosine * 100)
print ('END TIME: %s' % (time.time() - start))
