again = True
again2 = True
list = []
# 8=====D
while again == True:
    user_in = input("Bitte neues hinzuzufügendes Element angeben!\n")
    list.append(user_in)
    check = input("Weitere Elemente hinzufügen?\n")
    if "n" in check:
        again = False
while again2 == True:
    user_in2 = input("Zu entfernende Elemente eingeben!")
    if user_in in list:
        list.remove(user_in)
        check2 = input("Weitere Elemente hinzufügen?\n")
    if "n" in check:
        again2 = False
