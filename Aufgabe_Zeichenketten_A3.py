user_in = str(input("Bitte Zeichenkette eingeben, deren 3.; 6.; 9,; usw Zeichen ausgegeben werden sollen! \n"))
counter = 0
thirds = ""
for i in user_in:
    counter += 1
    if counter % 3 == 0:
        thirds += i
print(thirds)