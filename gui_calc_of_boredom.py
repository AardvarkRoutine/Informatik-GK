from tkinter import *
from tkinter.ttk import *
import math as m
root = Tk()
root.title("Calculator")
entry = Entry(root)
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
button_frame = Frame(root)
button_frame.grid(row=1,column=0,columnspan=4)
def calc(exp):
    try:
        return(eval(exp))
    except:
        return("Error")
def sqrt(exp):
    try:
        return(m.sqrt(exp))
    except:
        return("Error")
def power(exp):
    try:
        exp.replace("^", "**")
        return(eval(exp))
    except:
        return("Error")
button_list = [
    "7","8","9","+",
    "4","5","6","-",
    "1","2","3","*",
    ".","0","C","/",
    "^", "√", "CE", "="]
row = 0
column = 0
for button in button_list:
    if button == "=":
        command = lambda:entry.insert(END,calc(entry.get()))
    elif button == "√":
        command = lambda:entry.insert(END,sqrt(entry.get()))
    elif button == "^":
        command = lambda:entry.insert(END,power(entry.get()))
    elif button == "CE":
        command = lambda:entry.delete(0,END)
    elif button == "C":
        command = lambda:entry.delete(len(entry.get())-1,END)
    else:
        command = lambda:entry.insert(END,button)
    Button(button_frame,text=button,command=command).grid(row=row,column=column)
    column += 1
    if column > 3:
        column = 0
        row += 1
root.mainloop()