#!/usr/bin/env python
__author__ = "Caoimhe Harvey"

import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog
import NLPModule as nlp
import duplicationFunctions as df
from tkinter import messagebox
import subprocess

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Intro
        introduction = "This application is designed to help you manage and organize your" \
                       " harddrive in an\nefficient manner."
        Label(tab1, text=introduction).pack()

        # Main Widgets for Duplication: Tab2
        Button(tab2, text = "Choose a Directory", command=self.selectDirectory).pack()

        self.chosenDirectory = tk.Label(tab2)
        self.chosenDirectory.pack()

        Button(tab2, text="Find Duplicates", command=self.runDuplications).pack()
        self.processingLabel = tk.Label(tab2)
        self.processingLabel.pack()

        # Main widgets for file classifier
        Label(tab3, text="File Classification Module").pack()
        Label(tab3, text = "ONLY select .txt or .docx files").pack()
        Button(tab3, text = "Select File(s)", command = self.selectFile).pack()
        self.selectedFile = tk.Label(tab3)
        self.selectedFile.pack()
        Button(tab3, text="Find Appropiate Folder", command=self.findAppropiateFolder).pack()
        self.resultLabel = Label(tab3)
        self.resultLabel.pack()


    def selectDirectory(self):
        directory = filedialog.askdirectory()
        self.chosenDirectory.config(text= directory)

    def runDuplications(self):
        self.processingLabel.config(text="Processing..")
        images, textfiles = df.traverse(self.chosenDirectory.cget("text"))
        self.processingLabel.config(text="")
        #TODO: Parsing and formatting on the returned values
        Label(tab2, text= textfiles).pack()

    def selectFile(self):
        file_path = filedialog.askopenfilename(filetypes = (("docx files","*.docx"),("text files","*.txt")))
        self.selectedFile.config(text=file_path)

    def findAppropiateFolder(self):
        global oldPath, newPath
        oldPath = self.selectedFile.cget(("text"))
        newPath = nlp.performClassification(oldPath)
        if newPath != "":
            self.checkMove(oldPath, newPath)
        else:
            self.resultLabel.config(text = "Could not find appropiate folder")

    def checkMove(self, oldPath, newPath):
        answer = messagebox.askyesno("Move file", "Would you like to move\n\n" + oldPath + "\n\nto the new location at:\n\n" + newPath)
        if answer:
            movingCommand = "mv " + oldPath + " " + newPath
            subprocess.call(movingCommand, shell=True)
            openNewLocation = messagebox.askyesno("New File Location",
                                                  "File is now located at:\n" + newPath + "\nWould you like to Reveal File in Finder?")
            if openNewLocation:
                subprocess.call(["open", "-R", newPath])
            self.resultLabel.config(newPath)
        else:
            messagebox.showinfo("Action Cancelled", "File will remain at\n"+ oldPath)


# **********************************
#
# Set up the application window
#
# **********************************
root = tk.Tk()
root.title("Final Year Project")
root.update()
root.geometry('600x200')
note = Notebook(root)

# Set up main window
tab1 = Frame(note)

# Set up duplication window
tab2 = Frame(note)

# Set up file classifier window
tab3 = Frame(note)

note.add(tab1, text="Main")
note.add(tab2, text="Duplicates")
note.add(tab3, text="File Classifier")
note.pack()

app = Application(master=root)
app.mainloop()