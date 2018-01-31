from collections import defaultdict
from difflib import SequenceMatcher

arr = ['one', 'two', 'three', 'one', 'ocne', 'two', 'montana', 'once', 'onces', 'twos', 'spain', 'spanish', 'espanola', 'mountain',
       'ciara', 'ciaran', 'tree']
dd = defaultdict(list)

def f(word, list):
    size = len(list)
    c = 0
    for key, value in list.items():
        if word in list.keys():
            #if word is a key then skip
            return "skip",""
        else:
            #before creating a new key, check if it is similar to already existing keys
            if SequenceMatcher(None, word, key).ratio() > 0.7:
                return "add", key
            elif c != size:
                continue
            elif c == size:
                return "new", ""
        c += 1
    return "new", ""

for i in range(len(arr)):
    if(len(dd) == 0):
        dd[arr[i]]
    else:
        r , key = f(arr[i], dd)
        if r == "add":
            dd[key].append(arr[i])
        elif r == "new":
            dd[arr[i]]
        elif r == "skip":
            continue

for key, value in dd.items():
    print (key, value)

