#!/usr/bin/env python
__author__ = "Caoimhe Harvey"
import tkinter as tk
from tkinter.ttk import *
import collections

notebook_tabs = []
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        for tab in range(len(notebook_tabs)):
            Label(notebook_tabs[tab], text = "This is " + tab_names[tab]).pack()
            for key, value in list_of_tabs.items():
                if(key == tab_names[tab]):
                    Label(notebook_tabs[tab], text = value).pack()

list_of_tabs = {'Tab1':'string1', 'Tab2':'string2', 'Tab3':'string3', 'Tab4':'string4'}
tab_names = []
for key, value in list_of_tabs.items():
    tab_names.append(key)
print(tab_names)

def createTabs():
    note = Notebook(root)
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