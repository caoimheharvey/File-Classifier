#!/usr/bin/env python
# *************************************************************
#
#   File: main.py
#
#   This file runs the interface for the final year project. From the interface the user
#   can access the two modules: file classification, and locating duplicate (or similar)
#   files.
#
# *************************************************************

__author__ = "Caoimhe Harvey"

import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog
import fileclassification as nlp
import findduplicates as df
from tkinter import messagebox
import subprocess

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Intro
        introduction = df.checkextension('./gui-intro.txt')
        Label(tab1, text=introduction).pack()
        #
        # Main Widgets for Duplication: Tab2
        #
        string="This tab allows you to locate files in a directory which are 70% or more similar."
        Label(tab2, text = string).pack()
        Button(tab2, text = "Choose a Directory", command=self.selectDirectory).pack()

        self.chosenDirectory = tk.Label(tab2)
        self.chosenDirectory.pack()

        Button(tab2, text="Find Duplicates", command=self.findDuplicates).pack()
        #
        # Main widgets for Tab3
        #
        Label(tab3, text="This tab is designed to help you organize your files a lot easier.\nSimply select a file you wish to move.").pack()
        Label(tab3, text = "Then let the system find the best suited folder for the chosen file based\non the content in that file.").pack()
        Button(tab3, text = "Select File(s)", command = self.selectFile).pack()
        self.selectedFile = tk.Label(tab3)
        self.selectedFile.pack()
        Button(tab3, text="Find Appropiate Folder", command=self.findAppropiateFolder).pack()
        self.resultLabel = Label(tab3)
        self.resultLabel.pack()

    # *************************************************************
    #
    #   Functions for Tab 2: Duplicate locator GUI
    #
    # *************************************************************
    def selectDirectory(self):
        directory = filedialog.askdirectory()
        self.chosenDirectory.config(text= directory)

    def findDuplicates(self):
        global images, textfiles
        textfiles = df.findDuplicates(self.chosenDirectory.cget("text"))
        self.duplicationResultsWindow()


    #
    #   Duplication Results Window
    #
    def duplicationResultsWindow(self):
        global window1
        window1 = tk.Toplevel(note)
        window1.title("Duplication Finder Results")
        Label(window1, text = "Use the checkboxes to select all the files you wish to remove. Then click \"Delete\"").pack()
        global notebook_tabs, tab_names, variables, checkbox_string
        notebook_tabs = []
        tab_names = []
        for key, value in textfiles.items():
            tab_names.append(key)
        self.createTabs()
        variables = []
        checkbox_string = []

        for tab in range(len(notebook_tabs)):
            for key, value in textfiles.items():
                if(key == tab_names[tab]):
                    # Preview the duplicated file
                    text=df.checkextension(key)
                    Label(notebook_tabs[tab], text = "File Preview:\n\n", font = ('Helvetica', 16)).pack()
                    Label(notebook_tabs[tab], text=text[:255]).pack()
                    # Output the paths relating to the file
                    var = tk.IntVar()
                    variables.append(var)
                    checkbox_string.append(key)
                    Label(notebook_tabs[tab], text="\n\nFiles with this text or similar text are:\n",font = ('Helvetica', 16)).pack()
                    Checkbutton(notebook_tabs[tab], text = key, variable = var).pack()

                    for v in value:
                        var = tk.IntVar()
                        variables.append(var)
                        checkbox_string.append(v)
                        Checkbutton(notebook_tabs[tab], text=v, variable=var).pack()

        Button(window1, text = "Remove Selected Files", command = self.removeFiles).pack(side="right")

    def createTabs(self):
        style = Style(window1)
        style.configure('lefttab.TNotebook', tabposition='wn')
        note = Notebook(window1, style='lefttab.TNotebook')
        for tab in tab_names:
            t = Frame(note)
            fullpath = tab.split('/')
            actualtab = fullpath[len(fullpath)-1]
            notebook_tabs.append(t)
            note.add(t, text=actualtab)
        note.pack()

    def removeFiles(self):
        for i in range(len(variables)):
            if variables[i].get() == 1:
                bashCommand = "mv " + checkbox_string[i] + " /Users/CaoimheHarvey/.Trash"
                process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
                process.communicate()

        messagebox.showinfo("Files moved to trash", "All selected files have been have\nbeen moved to the trash.")


    def groupFilesinFolder(self):
        messagebox.showinfo("Select Root Folder", "In the following window, please select\nthe root folder you want to \nmove all "
                                                  "selected files to.")
        newRootFolder = filedialog.askdirectory()
        folderName = "newFolder"
        newPath = newRootFolder + "/" + folderName
        for i in range(len(variables)):
            if variables[i].get() == 1:
                subprocess.call(['./moveToNewFolder.sh', newRootFolder, folderName, checkbox_string[i], newPath])
        subprocess.call(["open", "-R", newPath])

    # *************************************************************
    #
    #   Functions for Tab 3: File Classifier GUI Functionality
    #
    # *************************************************************

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
        old_Path = oldPath.split('/')
        old = str(old_Path[len(old_Path)-2]) + "/" +str(old_Path[len(old_Path)-1])
        new_Path = newPath.split('/')
        new = str(new_Path[len(new_Path)-2]) + "/" +str(old_Path[len(old_Path)-1])
        print(old, new)
        answer = messagebox.askyesno("Move file", "Would you like to move\n\n" + old + "\n\nto the new location at:\n\n" + new)
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