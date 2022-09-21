# This script is the solution for the bmi calculator asked in task 2, from Paul and Max-Leon
try:
    weight_in_kg = input("Bitte geben sie ihr Körpergewicht in kg ein, statt eines Kommas bitte einen Punkt nutzen: Bsp.: 67.3kg \n")
    # Ask for user input to defeine their weight in kg

    size_in_m = input("Bitte geben sie ihre Körpergröße in m ein, statt eines Kommas bitte einen Punkt nutzen: Bsp.: 1.76m \n")
    # Ask for user input to define their size in m
    weight_in_kg = weight_in_kg.lower()
    size_in_m = size_in_m.lower()
    # set all characters in string to lowercase

    if "kg" in weight_in_kg :
        weight_in_kg = weight_in_kg.strip("kg")
    if "m" in size_in_m:
        size_in_m = size_in_m.strip("m")
    # remove unit descriptor from user input

    size_in_m = float(size_in_m)
    weight_in_kg = float(weight_in_kg)
    # force-convert objects above to floats 
    bmi = round(weight_in_kg / (size_in_m**2), 2)
    # Calculate BMI from pre-processed values
except:
    print("An error has occurred, please restart!")
    # show error message in case of exception

else: 
    print("Ihr BMI lautet:", bmi,", gerundet auf 2 Nachkommastellen")
    # Output of calculated bmi
    
