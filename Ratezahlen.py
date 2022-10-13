import random as r
repeat = True
counter = 0
while repeat == True:
    gen()
    guess_loop()
    input_repeat()
print("Danke fürs Spielen und bis zum nächsten Mal")

def gen():
    min = int(input("Geben Sie die untere Grenze des Zahlenbereichs an!"))
    max = int(input("Geben Sie die obere Gtenze des Zahlenbereichs ein!"))
    goal = r.randint(min, max)

def guess_loop():
    counter = 0
    hit = int(input("Geben sie die von ihnen erratene Zahl ein!"))
    while hit != goal:
        print("Kein Treffer; nochmal!")
        counter = counter +1
    else:
        print("Treffer! Sie haben im Zahlenbereich ", min," bis ", max,", ", counter, "Versuche gebraucht, um die Zahl zu erraten!")
        counter = 0

def input_repeat():
    repeat_in = input("Wollen sie nochmal spielen? (y / n):\n")
    if "n" in repeat_in:
        repeat = False