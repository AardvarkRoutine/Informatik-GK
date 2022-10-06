import random as r
print("Würfelspiel: Geben sie eine Zahl von 1-6 als Tipp an; anschließend weden 3 Würfel geworfen und gezählt, wie oft die von ihnen getippte Augenzahl vorkommt")
tip = int(input("Geben sie ihren Tipp ein!\n"))
while_counter = 0
win_counter = 0
while while_counter < 3:
    dice = r.randint(1, 6)
    if dice == tip:
        win_counter = win_counter + 1
    while_counter = while_counter +1
if win_counter != 0:
    print("Die von ihnen getippte Augenzahl wurde", win_counter, "x gewürfelt!")
else:
    print("Sie sind ein Verlierer! DIe von ihnen getippte Augenzahl kam nicht vor! ") 