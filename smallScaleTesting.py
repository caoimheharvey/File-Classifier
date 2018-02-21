# Import the os module, for the os.walk function
import os
from collections import defaultdict
# Empty dictionary of all text-file paths in the directory and their category
allTextFiles = defaultdict(list)
# Set the directory you want to start from
rootDir = '/Users/CaoimheHarvey/Desktop/Mock_Environment'
for dirName, subdirList, fileList in os.walk(rootDir):
    folders = dirName.split('/')
    folderName = folders[len(folders)-1]
    for fname in fileList:
        if fname.endswith('.txt'):
             allTextFiles[folderName].append(dirName + "/"+ fname)
data = []
# Parsing the value list into string to be stored with the key
counter = 0
for key, value in allTextFiles.items():
    itemsArray = (str(value).split(","))
    for item in itemsArray:
        if(counter + 1 == len(itemsArray)):
            print(key, item[2:-2])
            data.append({"class": key, "sentence": open(item[2:-2], 'r').read()})
        else:
            item = item[2:-1]
            if item.endswith(".txt\'"):
                item = str(item)[:-1]
            print(key, item)
            data.append({"class": key, "sentence": open(item, 'r').read()})
        counter +=1
