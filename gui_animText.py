from tkinter import *
import time

root = Tk()
root.title("Animation")
root.geometry("100x100")
root.configure(bg="black")

rgb = "red"
txt = "This is a test!"

label1 = Label(root, text=txt, font=("Arial", 10), bg="black", fg=rgb)
label1.place(x=0, y=0, width=100, height=100)

def changeColor():
    global rgb
    if rgb == "red":
        rgb = "green"
    elif rgb == "green":
        rgb = "blue"
    elif rgb == "blue":
        rgb = "red"
    label1.configure(fg=rgb)
    root.update()

while True:
    changeColor()
    time.sleep(0.5)

root.mainloop()
