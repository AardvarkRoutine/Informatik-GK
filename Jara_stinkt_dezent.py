# 8=====D
list = []
while repeat == True:
    user_in = input("Bitte neues hinzuzufügendes Element angeben!\n")
    list = list + [user_in]
    check = input("Weitere Elemente hinzufügen?\n")
    if "n" in check:
        repeat = False