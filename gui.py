from tkinter import Tk
from tkinter import filedialog
import methods

Tk().update()
Tk().withdraw()
directory = filedialog.askdirectory()
print(directory)

methods.traverse(str(directory))
