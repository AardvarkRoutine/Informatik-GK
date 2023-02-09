from tkinter import *
root = Tk()
root.title("Tic Tac Toe")
root.geometry("320x630")
root.config(bg="white")
canvas1 = Canvas(root, width=300, height=300, bg="white")
canvas1.grid(row=0, column=0, padx=10, pady=10, columnspan=3, rowspan=3)
canvas1.create_line(100, 0, 100, 300, fill="black", width=5)
canvas1.create_line(200, 0, 200, 300, fill="black", width=5)
canvas1.create_line(0, 100, 300, 100, fill="black", width=5)
canvas1.create_line(0, 200, 300, 200, fill="black", width=5)

button_globalpad = 25

buttona1 = Button(root, text=" ", font=("Arial", 20), bg="white", fg="black")
buttona2 = Button(root, text=" ", font=("Arial", 20), bg="white", fg="black")
buttona3 = Button(root, text=" ", font=("Arial", 20), bg="white", fg="black")
buttonb1 = Button(root, text=" ", font=("Arial", 20), bg="white", fg="black")
buttonb2 = Button(root, text=" ", font=("Arial", 20), bg="white", fg="black")
buttonb3 = Button(root, text=" ", font=("Arial", 20), bg="white", fg="black")
buttonc1 = Button(root, text=" ", font=("Arial", 20), bg="white", fg="black")
buttonc2 = Button(root, text=" ", font=("Arial", 20), bg="white", fg="black")
buttonc3 = Button(root, text=" ", font=("Arial", 20), bg="white", fg="black")

buttona1.grid(column=0, row=3, padx=button_globalpad, pady=button_globalpad, sticky="nsew")
buttona2.grid(column=1, row=3, padx=button_globalpad, pady=button_globalpad, sticky="nsew")
buttona3.grid(column=2, row=3, padx=button_globalpad, pady=button_globalpad, sticky="nsew")
buttonb1.grid(column=0, row=4, padx=button_globalpad, pady=button_globalpad, sticky="nsew")
buttonb2.grid(column=1, row=4, padx=button_globalpad, pady=button_globalpad, sticky="nsew")
buttonb3.grid(column=2, row=4, padx=button_globalpad, pady=button_globalpad, sticky="nsew")
buttonc1.grid(column=0, row=5, padx=button_globalpad, pady=button_globalpad, sticky="nsew")
buttonc2.grid(column=1, row=5, padx=button_globalpad, pady=button_globalpad, sticky="nsew")
buttonc3.grid(column=2, row=5, padx=button_globalpad, pady=button_globalpad, sticky="nsew")

root.mainloop()

for i in buttonList:
    if i%3 == 0:
        