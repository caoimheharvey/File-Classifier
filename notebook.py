import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def quit():
    global tkTop
    tkTop.destroy()


tkTop = tk.Tk()
tkTop.geometry('500x500')

tkLabelTop = tk.Label(tkTop, text="playing around with tabs")
tkLabelTop.pack()

notebook = ttk.Notebook(tkTop)
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text="Find Duplicates")
notebook.add(frame2, text="File Classifier")
notebook.pack()

tkButtonQuit = tk.Button(
    tkTop,
    text="Quit",
    command=quit)
tkButtonQuit.pack()

tkLabel = tk.Label(frame1, text="Hello Python!")
tkLabel.pack()

tkLabelVersion = tk.Label(frame2, text="Hello")
tkLabelVersion.pack()

tk.mainloop()
