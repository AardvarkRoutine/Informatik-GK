import random as r
counter = 0
rights = 0
points_counter = 0
games = int(input("Geben sie die Gewünschte Anzahl an Rechenaufgaben an!\n"))
while counter < games:
    a = r.randint(1, 100)
    b = r.randint(1, 100)
    solution = int(inout("Geben sie ihre Lösung ein!\n"))
    if a + b == solution:
        counter = counter + 1
        rights = rights + 1
        points_counter = points_counter + 1
        print("Richtig gerechnet!")
    else:
        print("Falsch gerechnet!")
        points_counter = points_counter - 1
    print("Sie haben bis jetzt ", rights, "Aufgaben richtig gerechnet!")
    print("Ihre momentane Punktzahl lautet:", points_counter,"!")
