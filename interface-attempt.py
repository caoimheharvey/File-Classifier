#!/usr/bin/env python
__author__ = "Caoimhe Harvey"
import tkinter as tk
from tkinter.ttk import *
from collections import defaultdict

notebook_tabs = []
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        for tab in range(len(notebook_tabs)):
            Label(notebook_tabs[tab], text = "This is " + tab_names[tab]).pack()
            for key, value in allTabs.items():
                if(key == tab_names[tab]):
                    for v in value:
                        Label(notebook_tabs[tab], text = v).pack()


allTabs = defaultdict(list)
allTabs['Tab1'].append('string1')
allTabs['Tab1'].append('string1.1')
allTabs['Tab2'].append('string2')
allTabs['Tab3'].append('string3')
allTabs['Tab3'].append('string3.1')
print(allTabs)
tab_names = []
for key, value in allTabs.items():
    tab_names.append(key)
print(tab_names)

def createTabs():
    style = Style(root)
    style.configure('lefttab.TNotebook', tabposition='ws')
    note = Notebook(root, style='lefttab.TNotebook')
    for tab in tab_names:
        t = Frame(note)
        notebook_tabs.append(t)
        note.add(t, text = tab)
    note.pack()


# **********************************
#
# Set up the application window
#
# **********************************
root = tk.Tk()
root.title("Final Year Project")
root.update()
root.geometry('600x400')

createTabs()
app = Application(master=root)
app.mainloop()