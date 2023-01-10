from tkinter import *
textis = "Day"
textsetpoint = "Night"
bgis = "yellow"
bgsetpoint = "blue"

def ChangeState():
    global textis, textsetpoint, bgis, bgsetpoint
    textis , textsetpoint = textsetpoint, textis
    bgis, bgsetpoint = bgsetpoint, bgis
    # labelZahl.config(text=str(stand))
tkWindow = Tk()
tWindow.title("DayNight")
tkWindow.geometry('170x125')
labelDN = Label(master = tkfenster, text = "Day", bg = "yellow", font = ("Arial", 20))
labelDN.place(x=5, y=5, width=160, height=80)
button = Button(master=tkFenster, text="change", bg="blue", command=buttonNullClick)
button.place(x=45, y=90, width=50, height=30)

# tkWindow.mainloop()
