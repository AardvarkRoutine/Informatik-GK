# Dezimal zu Binär Rechner
a = int(input("Bitte geben sie die ins binäre System zu konvertierende Zahl ein!"))
# Es wird nach einer Zahl gefragt, die konvertiert werden soll
ergebnis = ""
# Damit das Programm funktionieren kann, muss die variable für das Ergebnis definiert werden, da das programm sie sonst nicht kennt
while a != 0:
    q=a//2
    r=a%2
    a=q
    # Die while-Schleife rechnet die Zahl mit dem vorgegebenen Algorithmus in eine binärzahl um
    ergebnis += str(r)
    # der Rest jedes Durchlaufes (jeweils eine weitere Ziffer der binären Zahl) wird zur variable ergebnis hinzugefügt,
    # welche am Ende die fertig berechnete Binärzahl enthält
print(ergebnis)
# Am Ende wird die Binärzahl ausgegeben


# Zur Erklärung: ergebnis += str(r) ist dasselbe wie ergebnis = ergebnis + str(r)
