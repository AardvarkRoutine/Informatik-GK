from tkinter import *

def calc():
    weight = float(entryweight.get())
    height = float(entryheight.get())
    bmi = weight/(height*height)
    bmi_out = str(round(bmi*10)/10)
    labelBMI.config(text=bmi_out)
    entryheight.delete(0, END)
    entryweight.delete(0, END)
    if bmi > 25:
        entryweight.insert(0, "FETT")
        entryheight.insert(0, "SACK!")

tkw = Tk()
tkw.title('BMI')
tkw.geometry('258x195')
labelweight = Label(master=tkw, bg='#FFCFC9', text='weight in kg:')
labelweight.place(x=54, y=24, width=100, height=27)
entryweight = Entry(master=tkw, bg='white')
entryweight.place(x=164, y=24, width=40, height=27)
labelheight = Label(master=tkw, bg='#FFCFC9', text='Größe in m:')
labelheight.place(x=54, y=64, width=100, height=27)
entryheight = Entry(master=tkw, bg='white')
entryheight.place(x=164, y=64, width=40, height=27)
buttonBerechnen = Button(master=tkw, bg='#FBD975', text='berechnen', command=calc)
buttonBerechnen.place(x=54, y=104, width=100, height=27)
labelBMIWert = Label(master=tkw, bg='#D5E88F', text='BMI-Wert:')
labelBMIWert.place(x=54, y=144, width=100, height=27)
labelBMI = Label(master=tkw, bg='gray', text='')
labelBMI.place(x=164, y=144, width=40, height=27)
tkw.mainloop()