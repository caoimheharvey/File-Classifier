"""
File where I rough test code before including it in the main files
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
                if paths[j] not in dd.keys() and paths[j] not in dd.values():
                   dd[paths[i]].append(paths[j])


for key, value in dd.items():
    print(key , value)