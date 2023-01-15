from tkinter import *
global current, setpoint, bgcurrent, bgsetpoint
current = 'Day'
setpoint = 'Night'
bgcurrent = 'lightyellow'
bgsetpoint = 'blue'

def ChangeState():
    global current, setpoint, bgcurrent, bgsetpoint
    current, setpoint = setpoint, current
    bgcurrent, bgsetpoint = bgsetpoint, bgcurrent
    
tkFenster = Tk()
tkFenster.title('DayNightMode')
tkFenster.geometry('170x125')
labelDayNight = Label(master=tkFenster, text=current, bg=bgcurrent, font=('Arial', 20))
labelDayNight.place(x=5, y=5, width=160, height=80)

ButtonChange = Button(master=tkFenster, text=setpoint, bg=bgsetpoint, command=ChangeState())
ButtonChange.place(x=45, y=90, width=80, height=30)
tkFenster.mainloop()

