from tkinter import *
import random as ra
import time as t
import requests as r
import socket


root = Tk()
root.title("9 Tic Tac Toe MP")
root.geometry("590x600")

global gameID, sub_canvases, PlayerX, PlayerO, ip, notify
gameID = 0
sub_canvases = []
PlayerX = False
PlayerO = False
ip = "http://192.168.178.62:5000"
notify = Label(root, text="", font=("Arial", 15), wraplength=150)


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

    notify = Label(root, text="", font=("Arial", 15), wraplength=150)
    notify.grid(row=1, column=3, rowspan=3, columnspan=2, padx=10, pady=10)

    new = Button(root, text="New Game", font=("Arial", 15), command=newGame())
    new.grid(row=4, column=0, columnspan=5, padx=10, pady=10)

    join = Button(root, text="Join", font=("Arial", 15), command=joinGame())
    join.grid(row=5, column=0, columnspan=5, padx=10, pady=10)

def clearScreen():
    for widget in root.winfo_children():
        if widget != notify:
            widget.destroy()
            notify.config(text="")

def cancel():
    clearScreen()
    startScreen()

def newGame():
    clearScreen()
    gameID = r.post(ip + "/create_game").json()["game_id"]
    PlayerX = True

    code = Label(root, text="Game ID: " + str(gameID), font=("Arial", 15))
    code.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    notify.grid(row=1, column=0, rowspan=3, columnspan=3, padx=10, pady=10)
    cancel = Button(root, text="Cancel", font=("Arial", 15), command=cancel)
    cancel.grid(row=4, column=0, columnspan=5, padx=10, pady=10)

    game_full = False
    while not game_full:
        response = r.get(ip + "/game/" + str(gameID))
        game = response.json()
        if game['player_o'] is not None:
            game_full = True
            clearScreen()
            stdGameLoop()
        else:
            notify.config(text=response.json()["error"])
            root.update()
            t.sleep(1)


def joinGame():


def stdGameLoop():
    global sub_canvas
    canvas = Canvas(root, width=400, height=400)
    canvas.pack() # NEED TO REMOVE IF IMPLEMENTING GRID

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
            sub_canvas = Canvas(canvas, width=133.33, height=133.33, bd=0, highlightthickness=0, bg = ra.choice(["red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "white"]))
            sub_canvas.place(x=x1, y=y1)
            sub_canvases.append(sub_canvas)

startScreen()

root.mainloop()
