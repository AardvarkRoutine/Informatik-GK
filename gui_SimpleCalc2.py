import tkinter as tk
from math import sqrt

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0,tk.END)
        entry.insert(tk.END,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(tk.END,"Error")

def square_root():
    expression = entry.get()
    try:
        result = sqrt(float(expression))
        entry.delete(0,tk.END)
        entry.insert(tk.END,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(tk.END,"Error")

def power():
    expression = entry.get()
    try:
        numbers = expression.split("^")
        result = float(numbers[0]) ** float(numbers[1])
        entry.delete(0,tk.END)
        entry.insert(tk.END,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(tk.END,"Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root)
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

button_frame = tk.Frame(root)
button_frame.grid(row=1,column=0,columnspan=4)

button_list = [
    "7","8","9","+",
    "4","5","6","-",
    "1","2","3","*",
    ".","0","C","/",
    "sqrt","^"
]

row = 0
column = 0

for button_text in button_list:
    if button_text == "sqrt":
        button = tk.Button(button_frame,text=button_text,width=5,height=2,command=square_root)
    elif button_text == "^":
        button = tk.Button(button_frame,text=button_text,width=5,height=2,command=power)
    else:
        button = tk.Button(button_frame,text=button_text,width=5,height=2,command=lambda text=button_text:entry.insert(tk.END,text))
    button.grid(row=row,column=column)
    column += 1
    if column > 3:
        column = 0
        row += 1

equal_button = tk.Button(button_frame,text="=",width=5,height=2,command=calculate)
equal_button.grid(row=4,column=3)
print(str(root.geometry))

root.mainloop()