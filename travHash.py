import os, hashlib
from functions import similarities as s
"""
rootDir = "./"
hashed = {}
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        if(fname.lower().endswith(('.txt','.jpg', '.jpeg'))):
            #hashed[os.path.realpath(dirName +"/"+ fname)] = hashlib.md5(fname.encode('utf-8')).hexdigest()
            
        else:
            continue
    if len(subdirList) > 0:
        del subdirList[0]

for key,value in hashed.items():
    print(key, value)
print("---------------- DONE ------------------")
"""
