import random as r
print("Würfelspiel: Geben sie eine Zahl von 1-6 als Tipp an; anschließend weden 24 Würfel geworfen und gezählt, wie oft die von ihnen getippte Augenzahl auf beiden in de jeweiligen Runde geworfenen Würfel vorkommt!")
tip = int(input("Geben sie ihren Tipp ein!\n"))
while_counter = 0
win_counter = 0
while while_counter != 24:
    dice_a = r.randint(1, 6)
    dice_b = r.randint(1, 6)
    if dice_a == dice_b and dice_a == tip:
        win_counter = win_counter + 1
    while_counter = while_counter + 1
if win_counter != 0:
    print("Die von ihnen getippte Augenzahl wurde", win_counter, "x auf beiden Wüfeln gleichzeitig gewürfelt!")
else:
    print("Sie sind ein Verlierer! DIe von ihnen getippte Augenzahl kam nie auf beiden Würfeln gleichzeitig vor! ")
    