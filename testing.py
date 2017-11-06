"""
This will be testing traversing files to initialize
them with tags.
Subsequently I will attempt to get all the similar files into
a data structure where they can be analysed more in depth for
similarity.
"""
import functions
from collections import defaultdict

paths = functions.findAllFiles('dublin')
dd = defaultdict(list)
# really bad time complexity O(2n)
# what about doing O(n/2) by using a seen thing
for i in range(len(paths)):
    for j in range(len(paths)):
        if hash(paths[i]) == hash(paths[j]):
            continue
        else:
            ratio = functions.simRatio(paths[i],paths[j])
            if(ratio > 0.70):
                dd[paths[i]].append(paths[j])
                #functions.checkRep(paths[i], paths[j], dd)

for key, value in dd.items():
    print(key , value)