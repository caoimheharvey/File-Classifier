from collections import defaultdict

import docx2txt

a = ['./text-files/file1.txt', './text-files/file1c.txt','./text-files/file2.txt','./text-files/file2.txt','./text-files/file3.txt'
      ,'./text-files/file4.txt','./text-files/file5.txt','./text-files/test.docx']
dd = defaultdict(list)

def comp (file, file_path, list):
    from difflib import SequenceMatcher
    size = len(list)
    ctr = 0
    for key, value in list.items():
        if file_path in list.keys():
            print("skip")
            return "skip",""
        else:
            if SequenceMatcher(None, file, open(key).read()).ratio() > 0.7:
                return "add", key
            elif ctr != size:
                continue
            elif ctr == size:
                return "new", ""
        ctr+=1
    return "new",""


def maincomp(arr):
    for i in range(len(arr)):
        if arr[i].lower().endswith('.docx'):
            file_string = docx2txt.process(arr[i])
        else:
            file_string = open(arr[i]).read()

        if(len(dd) == 0):
            dd[arr[i]]
        else:
            result, key = comp(file_string, arr[i], dd)
            if result == "add":
                dd[key].append(arr[i])
            elif result == "new":
                dd[arr[i]]
            elif result == "skip":
                continue

    for key, value in dd.items():
        print (key, value)

import os
list_text = []
for dirName, subdirList, fileList in os.walk("./", topdown=False):
    for fname in fileList:
        if fname.lower().endswith(('.txt', '.docx')):
            list_text.append(dirName + "/" + fname)
        else:
            continue
    if len(subdirList) > 0:
        del subdirList[0]

print(list_text)
maincomp(list_text)
