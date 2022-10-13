import random as r
points = 0
choices = [20, 30, "V"]
dice_1 = r.choice(choices)
dice_2 = r.choice(choices)
dice_3 = r.choice(choices)
if "V" in dice_1:
    if "V" in dice_2:
        points = dice_3
    else: points = dice_2 + dice_3

elif "V" in dice_2:
    if "V" not in dice_3:
        points = dice_3

elif "V" not in dice_1 and "V" not in dice_2 and "V" not in dice_3:
    points = dice_1 + dice_2 + dice_3

print("Die Würfel sind Der Reihenfolge nach folgendermaßen gefallen: ", dice_1, " ", dice_2, " ", dice_3, ", ihre Punktzahl ist", points, "Punkte!")