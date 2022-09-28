x = float(input("Bitte geben sie einen Punkt x an!\n"))
y = float(input("Bitte geben sie  einen Punkt y an!\n"))
m = float(input("Bitte geben sie die Steigung m an\n!"))
b = float(input("Bitte geben sie den y-Achsenabschnitt b an!\n"))
try:
    if y == m * x + b :
        print("Der Punkt x liegt auf dem Grafen der Funktion!")
    else:  
        print("Der Punkt x liegt NICHT auf dem Grafen der Funktion!")
except:
    print("An error has occurred!")