# Dieses Programm ist spezialisiert darauf, ein Vermehrungsmodell auf Basis von 2 Altersgruppen (jung, erwachsen, alt) zu berechnen, um die Ergebnisse in einer Tabellendatei auszugeben

jung = input("Bitte geben sie die Anzahl an jungen individuen an!\n")
erwachsene = input("Bitte geben sie die Anzahl an erwachsenen Individuen an!\n")
alte = input("Bitte geben sie die Anzahl an erwachsenen Individuen an!\n")
columns = input("Geben sie die Anzahl der gewünschten Iterationen an!")

from openpyxl import Workbook
filename = "Modell.xlsx"
workbook = Workbook()
sheet = workbook.active

counter = 1
while var < columns:
    