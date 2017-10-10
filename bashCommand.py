"""
Executes bash command from current folder

"""
bashCommand = "mkdir testFolder"
import subprocess
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
