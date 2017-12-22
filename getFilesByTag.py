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

from collections import defaultdict
from difflib import SequenceMatcher

arr = ["this", "that", "word", "this", "thiss", "words", "mississippi", "montana", "america", "spain", "espana", "espanol"]

dd = defaultdict(list)


for i in range(len(arr)):
    if arr[i] not in dd.keys():
        for key,value in dd.items():
            ratio = SequenceMatcher(None, arr[i], key).ratio()
            print(arr[i], key, ratio)
            if (ratio > 0.7):
                dd[key].append(arr[i])
            else:
                dd[arr[i]]

print(dd)