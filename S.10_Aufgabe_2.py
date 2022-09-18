# This script is the solution for the cm to inch calculator asked for in task 2, from Paul and Max-Leon
unit = input("Geben sie das zu konvertierende Maß mitsamt der dazugehörigen Einheit an (Bsp.: 6.8cm / 4.1inch\n")
unit = unit.lower()

try:
    if "cm" or "centimeter" or "zentimeter" in unit :
        unit = float(unit.translate(None, abcdefghijklmnopqrstuvwxyz))
        converted = round(unit / 2.54,