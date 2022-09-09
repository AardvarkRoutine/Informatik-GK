# This script is the solution for the breaking distance calculator asked for in task 2, from Paul and Max-Leon

try:
    speed = input("Bitte geben sie die Geschwindigkeit des Fahrzeugs in km/h ein, um Reaktions- Brems- und Anhalteweg zu berechnen. Bsp.:118 km/h \n")
    # ask for user input in order to detrermine vehicle speed

    speed = speed.lower()
    speed = speed.strip("km/h")
    speed = speed.strip("kmh")
    speed = float(speed)
    # process user input springs in order make is usable for calculation

    speed10 = speed / 10
    distance_till_reaction = speed10 * 3
    breaking_distance = speed10*speed10
    distance_till_hold = distance_till_reaction + breaking_distance
    # calculates the 3 values total asked for in task 2 via the given formulas

except:
    print("An error has occurred, please restart!")
     # show error message in case of exception
else:
    print("Ihr Reaktionsweg beträgt ca.", distance_till_reaction, "km/h, Ihr Bremsweg ca.", breaking_distance, "km/h, und die Zeit bis zum anhalten des Fahrzeugs ca.", distance_till_hold, "km/h.")
    # outputs final values to user