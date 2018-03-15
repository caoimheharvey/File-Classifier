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
        global images, textfiles
        images, textfiles = df.traverse(self.chosenDirectory.cget("text"))
        #TODO: Parsing and formatting on the returned values
        self.duplicationResultsWindow()


    # New Window Definition
    def duplicationResultsWindow(self):
        global window1
        window1 = tk.Toplevel(note)
        window1.title("Duplication Finder Results")
        # window1.geometry("600x600")
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
                    text=df.checkextension(key)
                    Label(notebook_tabs[tab], text=text[:255]).pack()
                    # Label(notebook_tabs[tab], text=key).pack()
                    var = tk.IntVar()
                    variables.append(var)
                    checkbox_string.append(key)
                    Checkbutton(notebook_tabs[tab], text = key, variable = var).pack()
                    for v in value:
                        var = tk.IntVar()
                        variables.append(var)
                        checkbox_string.append(v)
                        Checkbutton(notebook_tabs[tab], text=v, variable=var).pack()

        Button(window1, text = "Remove Selected Files", command = self.removeFiles).pack(side="right")
        Button(window1, text = "Move Selected Files to a folder", command = self.groupFilesinFolder).pack(side="right")
        Button(window1, text = "Show selected files", command = self.showSelected).pack(side="right")

    # TODO: Finish the functions
    def showSelected(self):
        for i in range(len(variables)):
            if variables[i].get() == 1:
                print(str(i) + ":\t" + str(variables[i].get()) + "\t" + checkbox_string[i])
        print("\n")

    def removeFiles(self):
        pass

    def groupFilesinFolder(self):
        pass

    def createTabs(self):
        style = Style(window1)
        style.configure('lefttab.TNotebook', tabposition='wn')
        note = Notebook(window1, style='lefttab.TNotebook')
        for tab in tab_names:
            t = Frame(note)
            notebook_tabs.append(t)
            note.add(t, text=tab)
        note.pack()

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