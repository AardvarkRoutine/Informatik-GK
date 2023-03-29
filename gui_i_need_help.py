from tkinter import *
from tkinter.ttk import *
import math as m
root = Tk()
root.title("Calculator")
entry = Entry(root)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
button_frame = Frame(root)
button_frame.grid(row=1, column=0, columnspan=4)
history_frame = Frame(root)
history_frame.grid(row=0, column=5, columnspan=5)
def calc():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        err()
def sqrt():
    try:
        result = m.sqrt(float(entry.get()))
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        err()
def power():
    try:
        exp = entry.get().replace("^", "**")
        result = eval(exp)
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        err()
def err():
    entry.delete(0, END)
    entry.insert(END, "Error")
def clear():
    entry.delete(0, END)
def clear_last():
    entry.delete(len(entry.get())-1, END)
button_list = ["7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*",".", "0", "C", "/","^", "√", "CE", "="]
row, column = 0, 0
commands = {'=': calc,'√': sqrt,'^': power,'CE': clear,'C': clear_last}
for button in button_list:
    if button in commands:
        command = commands[button]
    else:
        command = lambda b=button: entry.insert(END, b)
    Button(button_frame, text=button, command=command).grid(row=row, column=column)
    column += 1
    if column > 3:
        column = 0
        row += 1
root.mainloop()