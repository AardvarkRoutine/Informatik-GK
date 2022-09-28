try:
    weight_in_kg = input("Bitte geben sie ihr Körpergewicht in kg ein, statt eines Kommas bitte einen Punkt nutzen: Bsp.: 67.3kg \n")

    size_in_m = input("Bitte geben sie ihre Körpergröße in m ein, statt eines Kommas bitte einen Punkt nutzen: Bsp.: 1.76m \n")
    weight_in_kg = weight_in_kg.lower()
    size_in_m = size_in_m.lower()

    if "kg" in weight_in_kg :
        weight_in_kg = weight_in_kg.strip("kg")
    if "m" in size_in_m:
        size_in_m = size_in_m.strip("m")

    size_in_m = float(size_in_m)
    weight_in_kg = float(weight_in_kg)

    bmi = round(weight_in_kg / (size_in_m**2), 2)

except:
    print("An error has occurred, please restart!")

else:
    if bmi <= 19 and bmi >= 26:
        print("Ihr BMI lautet:", bmi,", Normalgewicht, gerundet auf 2 Nachkommastellen")
    elif bmi < 19:
        print("Ihr BMI lautet:", bmi,", Untergewicht, gerundet auf 2 Nachkommastellen")
    else:
        print("Ihr BMI lautet:", bmi,", Übergewicht, gerundet auf 2 Nachkommastellen")