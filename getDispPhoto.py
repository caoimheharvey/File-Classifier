"""
Module to get and display photos to the user from a certain date range.
"""

import os
from collections import defaultdict
import time
import dateztime
start = time.time()
imageTable = defaultdict(list)
startdate = datetime.datetime(2017, 11, 1)
enddate = datetime.datetime(2017, 12, 1)
for dirName, subdirList, fileList in os.walk("./", topdown = False):
    for fname in fileList:
        if (fname.lower().endswith(('.jpg', '.jpeg', '.png'))):
            print(dirName + "/" + fname + "\t\t\t\t" + "Last modified: %s" % time.ctime(os.path.getmtime(dirName + "/" + fname)))
        else:
            continue
    if len(subdirList) > 0:
        del subdirList[0]
print("----------------- RESULTS --------------------")
print("Start date: " + str(startdate) + "\t\tEnd Date: " + str(enddate))
for key, value in imageTable.items():
    print(key, value)
print("Total Time: " , time.time() - start)
print("---------------- PROGRAM ENDED ------------------")