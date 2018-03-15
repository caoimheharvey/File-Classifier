from tkinter import *
from collections import defaultdict
master = Tk()

array = ['checkOne', 'checkTwo', 'checkThree', 'checkFour']
dict = defaultdict(list)
dict['checkOne'].append('content1')
dict['checkOne'].append('content2')
dict['checkTwo'].append('content3')
dict['checkThree'].append('content4')
dict['checkFour'].append('content5')
dict['checkOne'].append('content6')
dict['checkThree'].append('content7')

print(dict)
keyVars = []
valVars = []
checkboxes = []
checkbutton_string = []
def var_states():
    for i in range(len(checkbutton_string)):
        print(str(i) + "\t" + str(keyVars[i].get())+ "\t" + str(checkbutton_string[i]))

for i in range(len(dict)):
    v = IntVar()
    keyVars.append(v)
    valVars.append(v)

for key, value in dict.items():
    var = IntVar()
    keyVars.append(var)
    Checkbutton(master, text = key, variable = var).pack()
    checkbutton_string.append(key)
    for v in value:
        var = IntVar()
        keyVars.append(var)
        Checkbutton(master, text = v, variable = var).pack()
        checkbutton_string.append(v)
var_states()

Button(master, text='Show', command=var_states).pack()
mainloop()