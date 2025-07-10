#Calculator sum input

import tkinter as tk
from tkinter import ttk
from random import choice

def result_second_app():
    text_r = entry3.get().split('+')#Separate"+"

    len_Entry = len(text_r)
    dict1 = {}
    result = 0
    for i in range(1 , len(text_r)+1):#Variables name
        number_name = f"num{i}"
        dict1[number_name] = text_r[i-1]
    for i in range(1 , len_Entry + 1):#Variables value
        name = f"num{i}"
        result += int(dict1.get(name))

    label2.config(text= result)

#Run
window = tk.Tk()
window.title("python")
window.geometry("600x500")

#wigets
entry3 = ttk.Entry(window)
entry3.pack()

label2 = ttk.Label(window , width= 10 , background= "pink" , anchor= "center")
label2.pack()

button2 = ttk.Button(window , text= "=" , command= result_second_app)
button2.pack()


#show_tabel
window.mainloop()