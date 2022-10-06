import random as r

counter = 0
repeat = True

while repeat != False:
    min = int(input("Geben sie die untere Grenze des Zahlenbereichs ein!\n"))
    max = int(input("Geben sie die obere Grenze des Zahlenbereichs ein!\n"))
    goal = r.randint(min, max)
    user_in = int(input("Geben sie die von ihnen geratene Zahl ein!\n"))
    
    while user_in != goal:
        if user_in < goal:
            print("Die von ihnen geratene Zahl ist kleiner als die Trefferzahl!")
        elif user_in > goal:
            print("Die von ihnen geratene Zahl ist kleiner als die Trefferzahl!")
        else:
            print("Die von ihnen geratene Zahl liegt nicht im Zahlenbereich!")
            counter = counter +1
        user_in = int(input("Geben sie die von ihnen geratene Zahl ein!\n"))
    print("Treffer! Sie haben ",counter, " Versuche benötigt!" )
    repeat = input("Nochmal? (y, n\n")
    if "n" in repeat:
        repeat = False
        