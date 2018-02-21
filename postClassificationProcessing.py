# Post classification processing
import os
def export(fName):
    rootDir = '/Users/CaoimheHarvey/Desktop/Mock_Environment'
    for dirName, subdirList, fileList in os.walk(rootDir):
        folders = dirName.split('/')
        folderName = folders[len(folders) - 1]
        print(dirName)
        if(folderName == fName):
            oldPath = "/Users/CaoimheHarvey/desktop/test_files/Impressionism.txt"
            newPath = dirName
            bashCommand = "mv " + oldPath + " " + newPath
            import subprocess
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            # Terminate the process as file is to be allocated to only 1 folder
            # the one which it most closely matches
            exit(0)



l = [['History', 0.64702368657071108], ['Art', 0.50641326471227299]]

for item in l:
    for v in item:
        if(type(v) == str):
            export(v)

