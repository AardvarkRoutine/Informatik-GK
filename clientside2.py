from tkinter import *
import random as ra
import time as t
import requests as req

root = Tk()
root.title("9 Tic Tac Toe MP")
root.geometry("590x600")

global notify, game_id, sub_canvases, playerX, playerO
notify = Label(root, text="", font=("Arial", 15), wraplength=150, bg="grey80")
game_id = ra.randint(10, 99) # CHANGE FOR REAL IMPLEMENTATION
sub_canvases = []
playerX = False
playerO = False


def clearScreen():
    for widget in root.winfo_children():
        if widget != notify:
            widget.destroy()
            notify.config(text="")


def startScreen():

    global notify
    title = Label(root, text="Tic Tac Toe Multiplayer", font=("Arial", 20))
    title.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    disp = Canvas(root, width=400, height=400, bg="white")

    disp.create_line(0, 133, 400, 133, width=2)
    disp.create_line(0, 266, 400, 266, width=2)
    disp.create_line(133, 0, 133, 400, width=2)
    disp.create_line(266, 0, 266, 400, width=2)
    disp.grid(row=1, column=0, rowspan=3, columnspan=3, padx=10, pady=10)

    notify.grid(row=1, column=3, rowspan=2, columnspan=2, padx=10, pady=10)
    notify.config(text="Notification field")

    new = Button(root, text="New Game", font=("Arial", 15), command=newGame)
    new.grid(row=4, column=0, columnspan=5, padx=10, pady=10, sticky="ew")

    join = Button(root, text="Join", font=("Arial bold", 15), command=joinGame)
    join.grid(row=5, column=0, columnspan=5, padx=10, pady=10, sticky="ew")

def cancel():
    clearScreen()
    startScreen()


def newGame():
    clearScreen()
    title = Label(root, text="Game ID (enter in 'join game' on other host)", font=("Arial", 20))
    title.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    id = Label(root, text=game_id, font=("Arial", 15))
    id.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
    notify.grid(row=2, column=0, rowspan=2, columnspan=3, padx=10, pady=10)
    notify.config(text="Notification field")
    buttonC = Button(root, text="Cancel", font=("Arial", 15), command=cancel)
    buttonC.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
    
    response = req.post("http://" + ip + ":5000/newgame")
    game_id = response.json()["game_id"]
    id.config(text=game_id)
    
    loop = True
    while loop == True:
        response2 = req.get("http://" + ip + ":5000/game_state/" + str(game_id))
        if response2.status_code == 404:
            loop = False
            clearScreen()
            startScreen()
            notify.config(text=response2.json()["error"])
        elif response2.status_code==400:
            notify.config(text=response2.json()["error"])
            root.update()  
            t.sleep(1)
        else:
            loop = False
            mainGame()


def joinGame():
    clearScreen()
    title = Label(root, text="Enter Game ID", font=("Arial", 20))
    title.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    id = Entry(root, font=("Arial", 15), text = "ENTER ID HERE")
    id.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
    notify.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
    notify.config(text="Notification field")
    join = Button(root, text="Join", font=("Arial bold", 15), command=mainGame) # join function here
    join.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
    buttonC = Button(root, text="Cancel", font=("Arial", 15), command=cancel)
    buttonC.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
    
    response = req.post("http://" + ip + ":5000/join_game/" + str(id.get()))
    if response.status_code == 404 or response.status_code == 400:
        clearScreen()
        startScreen()
        notify.config(text=response.json()["error"])
    else:
        if game_id == response.json()["game_id"]:
            id.config(text=game_id)
            playerO = True
            mainGame()

def mainGame():
    clearScreen()
    global sub_canvas
    canvas = Canvas(root, width=400, height=400)
    canvas.grid(row=0, column=0, rowspan=3, columnspan=3, padx=10, pady=10)

    for i in range(1, 3):
        x = i * 133.33
        canvas.create_line(x, 0, x, 400, fill="black")

    for i in range(1, 3):
        y = i * 133.33
        canvas.create_line(0, y, 400, y, fill="black")

    for i in range(3):
        for j in range(3):
            x1 = j * 133.33
            y1 = i * 133.33
            x2 = x1 + 133.33
            y2 = y1 + 133.33
            sub_canvas = Canvas(canvas, width=133.33, height=133.33, bd=0, highlightthickness=0, bg = ra.choice(["red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "white"])) # CHANGE FOR REAL IMPLEMENTATION
            sub_canvas.place(x=x1, y=y1)
            sub_canvases.append(sub_canvas)

    def buttonPress(nr):
        
        if playerO == True:
            sub_canvases[nr].create_oval(0, 0, 133.33, 133.33, fill="white")
        else:
            sub_canvases[nr].create_line(0, 0, 133.33, 133.33, fill="white")
            sub_canvases[nr].create_line(133.33, 0, 0, 133.33, fill="white")

    button0 = Button(root, font=("Arial", 15), command=lambda: buttonPress(0), width=5, height=2)
    button1 = Button(root, font=("Arial", 15), command=lambda: buttonPress(1), width=5, height=2)
    button2 = Button(root, font=("Arial", 15), command=lambda: buttonPress(2), width=5, height=2)
    button3 = Button(root, font=("Arial", 15), command=lambda: buttonPress(3), width=5, height=2)
    button4 = Button(root, font=("Arial", 15), command=lambda: buttonPress(4), width=5, height=2)
    button5 = Button(root, font=("Arial", 15), command=lambda: buttonPress(5), width=5, height=2)
    button6 = Button(root, font=("Arial", 15), command=lambda: buttonPress(6), width=5, height=2)
    button7 = Button(root, font=("Arial", 15), command=lambda: buttonPress(7), width=5, height=2)
    button8 = Button(root, font=("Arial", 15), command=lambda: buttonPress(8), width=5, height=2)

    root.geometry("590x670")

    button0.grid(row=3, column=0, padx=10, pady=10)
    button1.grid(row=3, column=1, padx=10, pady=10)
    button2.grid(row=3, column=2, padx=10, pady=10)
    button3.grid(row=4, column=0, padx=10, pady=10)
    button4.grid(row=4, column=1, padx=10, pady=10)
    button5.grid(row=4, column=2, padx=10, pady=10)
    button6.grid(row=5, column=0, padx=10, pady=10)
    button7.grid(row=5, column=1, padx=10, pady=10)
    button8.grid(row=5, column=2, padx=10, pady=10)
    notify.grid(row=0, column=3, rowspan=2, columnspan=2, padx=10, pady=10)
    notify.config(text="Notification field")

startScreen()
root.mainloop()