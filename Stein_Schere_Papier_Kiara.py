# Macht "random" nutzbar
import random

# Wählbare Möglichkeiten für das Programm
möglichkeiten = ("Schere","Stein" , "Papier")

# Spieler wählt Stein, Schere oder papier
spieler = input("Deine Wahl [Stein / Schere / Papier]: ")

# Das Programm eintscheidet sich zufällig für eins der 3 Möglichkeiten 
programm = random.choice(möglichkeiten)

# Wahl des Programms wird im Vorraus ausgegeben
print("Das Programm hat sich für", programm, "entschieden!")

# Es wird überprüft, ob ein Unentschieden Stattgefunden hat
if spieler == programm:
    print("Unentschieden")

# Es wird überprüft, ob der Spieler gewonnen hat
if spieler == "Schere" and programm == "Stein" or spieler == "Stein" and programm == "Schere" or spieler == "Papier" and programm == "Stein":
    print("Sie haben gewonnen!")

# Wenn wie oben überprüft kein Unentschieden stattgefunden hat, und der Spieler nicht gewonnen hat, hat nach ausschlussprinzip das
# Programm gewonnen. Deswegen kann man hier ein einfaches else benutzen
else:
    print("Das Programm hat gewonnen!")