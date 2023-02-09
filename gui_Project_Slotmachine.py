from tkinter import *
import random
tkw = Tk()
tkw.title("Slot Machine")
tkw.geometry("900x360")
#tkw.wm_attributes('-transparentcolor', 'cyan')
bgPic = PhotoImage(file="einHurensohn.ppm")
bgLabel = Label(tkw, image=bgPic)
bgLabel.place(x=0, y=0, width=900, height=360)

labelBank = Label(bgLabel, text="Bank: 1000", font=("Arial", 10), bg="cyan", fg="white")
labelBank.grid(row=0, column=3, padx=10, pady=10, sticky="ne")
labelBilanz = Label(bgLabel, text="Bilanz: 0", font=("Arial", 10), bg="cyan", fg="white")
labelBilanz.grid(row=0, column=3, padx=10, pady=10, sticky="se")

startButton = Button(tkw, text="Start", font=("Arial", 20), bg="green", fg="white")

tkw.mainloop()