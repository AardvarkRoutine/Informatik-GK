from collections import Counter
counter = 0
vokale = ["a", "e", "i", "o", "u", "ä", "ö","ü"]
user_in = str(input("Bitte geben Sie eine Zeichenkette ein, deren Vokale gezählt werden sollen!\n"))
user_in = user_in.lower()
for i in vokale:
    if user_in.count(i):
        counter += 1
print("Es sind", counter, " Vokale in", user_in, "!")