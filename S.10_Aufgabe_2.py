# This script is the solution for the cm to inch calculator asked for in task 2, from Paul and Max-Leon
import re
unit = input("Geben sie das zu konvertierende Maß mitsamt der dazugehörigen Einheit an (Bsp.: 6.8cm / 4.1inch\n")
unit = unit.lower()

if "cm" or "centimeter" or "zentimeter" in unit :
     unit = float(re.sub('\d, \D', ' ', unit))
     converted = round(unit / 2.54, 2)
     prefix = "cm"

elif "i" or "in" or "inch" in unit :
      unit = re.sub('\d, \D', ' ', unit)
      unit = float(unit.replace(",", "."))
      converted = round(unit * 2.54, 2)
      prefix = "inch"

print("Ihr Maß, umgerechnet in", prefix, ", ist:", unit)