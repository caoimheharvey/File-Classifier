from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

root = Tk()
root.geometry("600x400")
note = Notebook(root)
# **********************************
#
# Tab1: Main instruction and project description page
#
# **********************************
tab1 = Frame(note)
introduction = "This application is designed to help you manage and organize your harddrive in an\nefficient manner."
Label(tab1, text = introduction).pack()

# **********************************
#
# Tab2: Duplication finder module
#
# **********************************
tab2 = Frame(note)

Label(tab2, text = "This module does XYZ\n\n").pack()

def selectDirectory():
    directory = filedialog.askdirectory()
    print(directory)


Button(tab2, text = "Select Directory", command=selectDirectory).pack()
directoryLabel = Label(tab2, text = "directory path goes here").pack()

Button(tab2, text = "Scan for Duplicates").pack()

# **********************************
#
# Tab3: File classification module
#
# **********************************
tab3 = Frame(note)
Label(tab3, text = "You can only select .docx or .txt files.").pack()
Button(tab3, text = "Select File(s)").pack()


note.add(tab1, text = "Main")
note.add(tab2, text = "Duplicates")
note.add(tab3, text = "File Classification")
note.pack()
root.mainloop()
exit()