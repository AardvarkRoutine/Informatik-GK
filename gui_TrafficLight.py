from tkinter import *
import time as t

global state, active
active = False
state = 0

def state0():
    global state
    green.config(bg = "white")
    red.config(bg = "red")
    state = 0

def state1():
    global state
    yellow.config(bg = "yellow")
    state = 1

def state2():
    global state
    red.config(bg = "white")
    state = 2

def state3():
    global state
    yellow.config(bg = "white")
    green.config(bg = "green")
    state = 3

def reg():
    while active == True:
        state0()
        t.sleep(0.75)
        state1()
        t.sleep(0.75)
        state2()
        t.sleep(0.75)
        state3()
        t.sleep(0.75)

def shift():
    global state
    if state == 0:
        state1()
    elif state == 1:
        state2()
    elif state == 2:
        state3()
    elif state == 3:
        state0()
    else:
        print("You fucked up")
        
def active_flipflop():
    global active
    if active == True:
        active = False
    else:
        active = True
    reg()

tkw = Tk()
tkw.title("Ampel")
tkw.geometry("200x230")
tkw.config(bg = "white")
red = Label(master = tkw, text = "Stop", fg = "black", bg = "white", font = ("Arial", 16))
yellow = Label(master = tkw, text = "Achtung", fg = "black", bg = "white", font = ("Arial", 16))
green = Label(master = tkw, text = "Go!", fg = "black", bg = "white", font = ("Arial", 16))
red.place(x = 60, y = 5, width = 90, height = 30)
yellow.place(x = 60, y = 50, width = 90, height = 30)
green.place(x = 60, y = 95, width = 90, height = 30)

onoff = Button(master = tkw, text = " an / aus", fg = "black", bg = "gray", font = ("Arial", 12), command = active_flipflop)
shift = Button(master = tkw, text = "schalten", fg = "black", bg = "gray", font = ("Arial", 12),command = shift)
onoff.place(x = 65, y = 135, width = 70, height = 30)
shift.place(x = 65, y = 175, width = 70, height = 30)

tkw.mainloop()
