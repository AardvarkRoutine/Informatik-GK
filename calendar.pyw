from datetime import date as d
from datetime import datetime
from tkinter import *
def day_of_week():
    wday={
        0 : "Monday",
        1 : "Tuesday",
        2 : "Wednesday",
        3 : "Thursday",
        4 : "Friday",
        5 : "Saturday",
        6 : "Sunday",
        }
    dt = datetime.now()
    weekday_num = dt.weekday()
    weekday = wday[weekday_num]
    return weekday

today = d.today()
tkFenster = Tk()
tkFenster.title('Kalender')
tkFenster.geometry('130x145')
labelMonat = Label(master=tkFenster, text=today.strftime("%m"), fg='black', bg='white', font=('Arial', 16))
labelMonat.place(x=5, y=5, width=120, height=20)
labelTag = Label(master=tkFenster, text=today.strftime("%d"), fg='black', bg='#FFCFC9', font=('Arial', 72))
labelTag.place(x=5, y=30, width=120, height=80)
labelWochentag = Label(master=tkFenster, text=day_of_week())
labelWochentag.place(x=35, y=115, width=60, height=30)
