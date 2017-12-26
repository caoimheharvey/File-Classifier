"""
Find duplicate text files

import functions
from collections import defaultdict
paths = functions.findAllFiles('dublin')
dd = defaultdict(list)

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

"""
