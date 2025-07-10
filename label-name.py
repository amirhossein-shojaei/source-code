#Display first and last name on the label

from tkinter import *

def mynames():
    lbl.config(text= "my name is {} {}".format(name1.get(),name2.get()))#Label نمایش اسم و فامیل در

window = Tk()

Label(window,text= 'Firstname').pack()
name1 = Entry(window)
name1.pack()

Label(window,text= 'Lastname').pack()
name2 = Entry(window)
name2.pack()

Button(window,text= "click",command= mynames).pack()

lbl = Label(window,text= "")
lbl.pack()

window.geometry("400x300")
window.resizable(width= False,height= False)
window.mainloop()