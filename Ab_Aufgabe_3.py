year = int(input("Bitte die Jahreszahl eingeben! (yyyy), Bsp.: '2022'"))
try:
    if year % 4 == 0 and year % 100 ==0 :
        print("Das angegebene Jahr,", year, ", ist ein Schaltjahr!")

    elif year % 100 == 0 and year % 400 == 0:
        print("Das angegebene Jahr,", year, ", ist ein Schaltjahr!")
    else:
        print("Das angegebene Jahr,", year, ", ist KEIN Schaltjahr!")
except:
    print("An error has occurred!")