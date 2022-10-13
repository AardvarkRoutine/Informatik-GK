import random as r
counter = 0
repeat = True
player_tip = int(input("Tippen Sie in diesem Würfelspiel auf eine Zahl von 1 bis 6. Kommt diese Zahl auf beiden pro Runde geworfenen Würfeln vor, gewinnen sie!\n"))
while repeat == True:
    dice_1 = r.randint(1, 6)
    dice_2 = r.randint(1, 6)
    if dice_1 == dice_2:
        counter = counter + 1
        print("Sie gewinnen! Sie haben ", counter, " Versuche benötigt!")
        repeat = False
    else:
        repeat = True
        counter = counter + 1