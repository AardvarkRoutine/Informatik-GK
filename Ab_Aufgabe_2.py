sex = input("Bitte geben sie ihr biologisches Geschlecht an, 'm' für männlich, 'w' für weiblich")
age = input("Bitte geben sie ihr Alter in Jahren an!")
name = input("Bitte geben sie ihren Vornamen an!")
sirname = input("Bitte geben sie ihren Nachnamen an!")

if age < 18:
    print("Hallo,", name, "!")
else:
    if "m" in age:
        print("Guten Tag, Herr ", sirname, "!")
    elif "w" in age:
        print("Guten Tag, Frau ", sirname, "!")
    else:
        print("Guten Tag, ", name, "!")