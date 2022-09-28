import random as r
count = 0
games = int(input("Geben sie die gewünschte Anzahl an Spielen ein!"))
while count < games :
    a = r.randint(1, 100)
    b = r.randint(1, 100)
    print("Die Aufgabe lautet: ", a, "+", b)
    solution = int(input("bitte geben sie die von ihnnen ausgerechntet Lösung ein!\n"))

    while solution != a + b:
        print("Die von ihnen usgerechnete Lösung ist falsch, versuche es nochmal!")
        solution = int(input("bitte geben sie die von ihnnen ausgerechntet Lösung ein!\n"))
    print("Richtig!")
    count = count + 1
print("Die Rechenübung ist abgeschlossen!")