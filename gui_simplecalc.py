from tkinter import *
import time as t
def calc():
    try:
        num = int(entrynum.get())
    except ValueError:
        button.config(text = 'NOT A NUMBER!!')
        button.config(bg = 'red')
        tkw.update()
        t.sleep(0.2)
        button.config(bg = "white")
        tkw.update()
        t.sleep(0.2)
        button.config(bg = 'red')
        tkw.update()
        t.sleep(0.2)
        button.config(bg = "white")
        tkw.update()
        button.config(bg = 'lightgray')
        button.config(text = 'Check if prime number')
        return
    if num > 1 and num % num == 0:
        entrynum.delete(0, END)
        entrynum.insert(0, 'Prime number')
    else:
        entrynum.delete(0, END)
        entrynum.insert(0, 'Not a prime number')

tkw = Tk()
tkw.title('Test')
tkw.geometry('160x110')
entrynum = Entry(master=tkw, bg='white')
entrynum.place(x=30, y=40, width=100, height=30)
button = Button(master=tkw, bg ='lightgray', fg = 'black', text='Check if prime number', command=calc)
button.place(x=5, y=80, width=150, height=20)
tkw.mainloop()
