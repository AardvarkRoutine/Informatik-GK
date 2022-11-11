user_in = str(input("Bitte geben sie eine Zeichenkette ein, die encodiert werden soll!\n"))
char_shift = int(input("Geben Sie ein, um wieviele Stellen die Buchstaben im Alphabet verschoben werden sollen!\n"))
user_in = user_in.lower()
for x in user_in:
    if(x =="y"):
        print("a", end="")
    elif(x=="z"):
        print("b", end="")
    elif (ord(x) in range(97, 124)):
        conv = ord(x)
        x = conv+char_shift
        print(chr(x),end="")
    else:
        print(x, end="")
