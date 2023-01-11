from tkinter import *
def red():
    green.config(bg = "white")
    red.config(bg = "red")

def redYellow():
    yellow.config(bg = "yellow")

def yellow():
    red.config(bg = "white")


def green():
    yellow.config(bg = "white")
    green.config(bg = "green")





tkw = Tk()
tkw.title("Ampel")
tkw.geometry("200x230")
tkw.config(bg = "white")
tkw.focus_set()
tkw.bind("<Escape>", lambda e: e.widget.quit())
red = Label(master = tkw, text = "Stop", fg = "black", bg = "white", font = ("Arial", 16))
yellow = Label(master = tkw, text = "Achtung", fg = "black", bg = "white", font = ("Arial", 16))
green = Label(master = tkw, text = "Go!", fg = "black", bg = "white", font = ("Arial", 16))
red.place(x = 60, y = 5, width = 90, height = 30)
yellow.place(x = 60, y = 50, width = 90, height = 30)
green.place(x = 60, y = 95, width = 90, height = 30)

onoff = Button(master = tkw, text = " an / aus", fg = "black", bg = "gray", font = ("Arial", 12), )#command = 
shift = Button(master = tkw, text = "schalten", fg = "black", bg = "gray", font = ("Arial", 12), ) #command = 
onoff.place(x = 65, y = 135, width = 70, height = 30)
shift.place(x = 65, y = 175, width = 70, height = 30)

tkw.mainloop()
