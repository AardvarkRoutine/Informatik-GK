user_in = str(input("Bitte geben Sie die zu überprüfende Zeichenkette ein!\n"))
test_for = str(input("Bitte geben sie ein(e) Zeichen(kette) ein, nach der gesucht werden soll!\n"))
if test_for in user_in:
    print(test_for, " wurde in", user_in, " gefunden!")
else:
    print(test_for, " wurde nicht in", user_in, " gefunden!")