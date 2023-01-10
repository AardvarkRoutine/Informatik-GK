from tkinter import *

textis = "Day"
textsetpoint = "Night"
bgis = "yellow"
bgsetpoint = "blue"
global textis, textsetpoint, bgis, bgsetpoint, labelDN, button

def ChangeState():
    global textis, textsetpoint, bgis, bgsetpoint, labelDN, button
    textis , textsetpoint = textsetpoint, textis
    bgis, bgsetpoint = bgsetpoint, bgis
    labelDN.config(text = textis, bg = bgis)
    button.config(text = textsetpoint, bg = bgsetpoint)
button.config(command = ChangeState())

tkWindow = Tk()
tkWindow.title("DayNight")
tkWindow.geometry('170x125')


button = Button(master=tkWindow, text=textsetpoint, bg=bgsetpoint)

labelDN = Label(master = tkWindow, text = textis, bg = bgis, font = ("Arial", 20))
labelDN.place(x=5, y=5, width=160, height=80)

button = Button(master=tkWindow, text=textsetpoint, bg=bgsetpoint, command=ChangeState())
button.place(x=45, y=90, width=50, height=30)
tkWindow.mainloop()

def ChangeState():
    global textis, textsetpoint, bgis, bgsetpoint, labelDN, button
    textis , textsetpoint = textsetpoint, textis
    bgis, bgsetpoint = bgsetpoint, bgis
    labelDN.config(text = textis, bg = bgis)
    button.config(text = textsetpoint, bg = bgsetpoint)
button.config(command = ChangeState())

tkWindow.mainloop()
