#!/usr/bin/env python
__author__ = "Caoimhe Harvey"
# -----------------------------------------
# All code which is to be executed from the command line goes here
# -----------------------------------------
"""
Running bash commands from python
"""
def runBashCommand(bashCommand):
    import subprocess
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)
    return output

def cv2func():
    import subprocess
    command = "export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

"""
Adding a tag to a file or folder --- used to help identify the contents
"""
def addFileTag(tags, file_path):
    runBashCommand("tag -a " + tags + " " + file_path)

"""
searching current directory for all files/directories with a certain tag
"""
def findAllFiles(tags):
    paths = runBashCommand("tag -f " + tags)
