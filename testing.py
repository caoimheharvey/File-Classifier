#!/usr/bin/env python
__author__ = "Caoimhe Harvey"

import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog


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
        Button(tab2, text="Choose a Directory", command=self.selectDirectory).pack()

        self.chosenDirectory = tk.Label(tab2)
        self.chosenDirectory.pack()

        Button(tab2, text="Find Duplicates", command=self.runDuplications).pack()
        self.processingLabel = tk.Label(tab2)
        self.processingLabel.pack()

        # Main widgets for file classifier
        Label(tab3, text="File Classification Module").pack()
        Label(tab3, text="ONLY select .txt or .docx files").pack()
        Button(tab3, text="Select File(s)").pack()

    def selectDirectory(self):
        directory = filedialog.askdirectory()
        self.chosenDirectory.config(text=directory)

    def runDuplications(self):
        self.processingLabel.config(text="Processing..")
        import duplicationFunctions as df
        global images, textfiles
        images, textfiles = df.traverse(self.chosenDirectory.cget("text"))
        self.processingLabel.config(text="")
        # Open Results in new window
        self.duplicationResultsWindow()


    # New Window Definition
    def duplicationResultsWindow(self):
        window1 = tk.Toplevel(note)
        window1.geometry("600x600")

        # TODO: Parsing and formatting on the returned values
        l = Label(window1, text = "Click here to reveal in finder")
        l.bind("<Button-1>", self.openFile)
        l.pack()

    def openFile(self, file_to_show):
        file_to_show = "/Users/CaoimheHarvey/dropbox/year4/fyp/file-classifier/text-files/file1.txt"
        import subprocess
        subprocess.call(["open", "-R", file_to_show])



# **********************************
#
# Set up the application window
#
# **********************************
root = tk.Tk()
root.title("Final Year Project")
root.update()
root.geometry('600x400')
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
