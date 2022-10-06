import random as r
shapes = ["Stein", "Schere", "Papier"]
beats = {
    "Stein" : "Schere",
    "Papier" : "Stein",
    "Schere" : "Papier"
}
tie = True
while tie != False:
    player_input = input("Geben sie das von Ihnen gewählte Zeichen (Schere, Stein, Papier) ein:\n")
    program_input = r.choice(shapes)
    if program_input == beats[player_input]:
        print(player_input, "schlägt", program_input, ", Sie gewinnen!")
        tie = False
    elif player_input == beats[program_input]:
        print(program_input, "schlägt", player_input, ", das Programm gewinnt!")
        tie = False