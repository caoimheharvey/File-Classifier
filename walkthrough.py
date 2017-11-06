#!/usr/bin/env python
__author__ = "Caoimhe Harvey"

"""
Walkthrough
"""

import tkinter as tk
from tkinter import filedialog
import functions as f

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        self.selDir = tk.Button(self, text = "Choose a Directory")
        self.selDir["command"] = self.getDirectory
        self.selDir.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

        self.directoryLabel = tk.Label(self)
        self.directoryLabel.pack(side = "top")

        self.changeThis = tk.Label(self)
        self.changeThis.pack(side = "top")

    def getDirectory(self):
        directory = filedialog.askdirectory()
        self.directoryLabel.config(text= directory)
        print(directory)
        f.traverse(directory)

root = tk.Tk()
root.update()
root.geometry('500x300')
app = Application(master=root)
app.mainloop()
