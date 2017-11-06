"""
This will be testing traversing files to initialize
them with tags.
Subsequently I will attempt to get all the similar files into
a data structure where they can be analysed more in depth for
similarity.
"""

def traverse1(rootDir):
    import os
    import functions as fn
    from collections import defaultdict
    imageTable = defaultdict(list)
    for dirName, subdirList, fileList in os.walk(rootDir):
        print('Found directory: %s' % dirName)
        for fname in fileList:
            if(fname.lower().endswith(('.txt'))):
                fn.setTags(dirName + "/"+ fname, 4)
            elif(fname.lower().endswith(('.jpg', '.jpeg', '.png'))):
                hashedImage = fn.setHashValue(imageTable, dirName+ "/"+ fname)
                imageTable[hashedImage].append(dirName+ "/"+ fname)
            else:
                continue
        if len(subdirList) > 0:
            del subdirList[0]

    print(imageTable)
    print("---------------- DONE ------------------")


traverse1("./")