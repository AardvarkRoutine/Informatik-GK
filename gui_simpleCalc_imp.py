from tkinter import *
import math as m

tkw = Tk()
tkw.title('Simple Calculator')
tkw.geometry('500x230')

entry1 = Entry(master=tkw, text = "0", bg='lightgray', width='135')
entry1.place(x=10, y=10, width="135")
entry2 = Entry(master=tkw, text = "2" bg='lightgray', width='135')
entry2.place(x=155, y=10, width="135")
def add():
    try:
        num1 = entry1.get()
        num2 = entry2.get()
        num1 = float(num1)
        num2 = float(num2)
        ans = num1 + num2
        return ans
    except:
        return "Error"

def sub():
    try:
        num1 = entry1.get()
        num2 = entry2.get()
        num1 = float(num1)
        num2 = float(num2)
        ans = num1 - num2
        return ans
    except:
        return "Error"

def mul():
    try:
        num1 = entry1.get()
        num2 = entry2.get()
        num1 = float(num1)
        num2 = float(num2)
        ans = num1 * num2
        return ans
    except:
        return "Error"

def div():
    try:
        num1 = entry1.get()
        num2 = entry2.get()
        num1 = float(num1)
        num2 = float(num2)
        ans = num1 / num2
        return ans
    except:
        return "Error"

def sqrt():
    try:
        num1 = entry1.get()
        num2 = entry2.get()
        num1 = float(num1)
        ans = m.sqrt(num1)
        return ans
    except:
        if num2 >=0:
            return "sqrtError"
        else:
            return "Error"

def pot2():
    try:
        num1 = entry1.get()
        num2 = entry2.get()
        num1 = float(num1)
        num2 = float(num2)
        ans = num1 ** num2
        return ans
    except:
        return "Error"

global clicked
clicked = None

def click(func):
    global clicked
    clicked = func

def sol():
    global clicked
    solution = clicked()
    ansHistory.insert(END, solution, "\n")

ansHistory = Label(master=tkw, bg='lightgray', text='History')
ansHistory.place(x=300, y=0, width=200, height=300)

buttonAdd = Button(master=tkw, bg='#FFCFC9', text='+', command=clicked(add))
buttonAdd.place(x=10, y=50, width=62.5, height=50)
buttonSub = Button(master=tkw, bg='#FFCFC9', text='-', command=clicked=(sub))
buttonSub.place(x=82.5, y=50, width=62.5, height=50)
buttonMul = Button(master=tkw, bg='#FFCFC9', text='*', command=clicked=(mul))
buttonMul.place(x=155, y=50, width=62.5, height=50)
buttonDiv = Button(master=tkw, bg='#FFCFC9', text='/', command=clicked(div))
buttonDiv.place(x=227.5, y=50, width=62.5, height=50)
buttonSqrt = Button(master=tkw, bg='#FFCFC9', text='2. Wurzel', command=clicked(sqrt))
buttonSqrt.place(x=10, y=110, width=135, height=50)
buttonPot2 = Button(master=tkw, bg='#FFCFC9', text='^2', width='180', height = '40', command =click(pot2))
buttonPot2.place(x=155, y=110, width=135, height=50)
buttonAns = Button(master=tkw, bg='#FFCFC9', text='Ans', command=sol)
buttonAns.place(x=10, y=170, width=280, height=50)

tkw.mainloop()
