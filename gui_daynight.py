from tkinter import *
tkWindow = Tk()
tkWindow.title("DayNight")
tkWindow.geometry('170x125')
labelDN = Label(master = tkWindow, text = "Day", bg = "yellow", font = ("Arial", 20))
labelDN.place(x=5, y=5, width=160, height=80)
button = Button(master=tkWindow, text="Night", bg="blue")
button.place(x=60, y=90, width=50, height=30)
def ChangeState():
    global labelDN, button
    if labelDN["text"] == "Day":
        labelDN.config(text = "Night", bg = "blue")
        button.config(text = "Day", bg = "yellow")
    else:
        labelDN.config(text = "Day", bg = "yellow")
        button.config(text = "Night", bg = "blue")
button.config(command=ChangeState)
tkWindow.mainloop()
