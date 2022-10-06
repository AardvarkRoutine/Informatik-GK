import random as r
possible_spapes = ["Stein", "Schere", "Papier"]
stalemate = True

while stalemate != False:
    user_shape = input("Geben sie das Zeichen ihrer Whl ein (Stein, Schere, Papier)")
    program_shape = r.choice(possible_spapes)
    if program_shape == "Stein":
        if user_shape == "Papier":
            print("Papier umschließt Stein!\nSie gewinnen!")
        elif user_shape == "Schere":
            print("Stein schlägt Schere!\nDer Computer gewinnt!")
    if program_shape == "Schere":
        if user_shape == "Stein":
            print("Stein schlägt Schere!\nSie gewinnen!")
        elif user_shape == "Papier":
            print("Schere schneidet papier!\nDer Computer gewinnt!")
    if program_shape == "Papier":
        if user_shape == "Schere":
            print("Schere schneidet papier!\nSie gewinnen!")
        elif user_shape == "Stein":
            print("Papier umschließt Stein!\nDer Computer gewinnt!")
    else:
        print:("Das Programm und sie Haben das gleiche Zeichen", user_shape, "gewählt! Pat!")
        stalemate = False
    