from tkinter import *
master = Tk()

array = ['checkOne', 'checkTwo', 'checkThree', 'checkFour']
vars = []
checkboxes = []
def var_states():
   # print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))
    for i in range(len(array)):
        if(vars[i].get() == 1):
            print(str(i) + ":\t" + str(vars[i].get()))

for i in range(len(array)):
    v = IntVar()
    vars.append(v)

for i in range(len(array)):
    c = Checkbutton(master, text = array[i], variable=vars[i]).pack()
    checkboxes.append(c)

Button(master, text='Show', command=var_states).pack()
mainloop()