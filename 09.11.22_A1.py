# Dezimal zu 8-Bit binär Rechner
var = int(input("Bitte eine Zahl <256 eingeben, welche ins binärsystem konvertiert werden soll!\n"))
if var < 256:
    var_bin = str(bin(var))
    var_bin = var_bin.strip("0b")
    print(var, " konvertiert ins binäre System, lautet: ", var_bin)
else:
    print("Die von ihnen eingegebene Zahl ist ungültig!")