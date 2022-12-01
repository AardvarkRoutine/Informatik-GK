abc = {
    'a': 0,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5,
    "g" : 6,
    "h" : 7,
    "i" : 8,
    "j" : 9,
    "k" : 10,
    "l" : 11,
    "m" : 12,
    "n" : 13,
    "o" : 14,
    "p" : 15,
    "q" : 16,
    "r" : 17,
    "s" : 18,   
    "t" : 19,
    "u" : 20,
    "v" : 21,
    "w" : 22,
    "x" : 23,
    "y" : 24,
    "z" : 25
}
help = "abcdefghijklmnopqrstuvwxyz"
user_in = str(input("Bitte geben sie eine Zeichenkette ein, die encodiert werden soll!\n"))
abc_shift = (input("Geben sie einenen Buchstaben ein, der an Stelle von a stehen soll!\n"))
user_in = user_in.lower()
char_shift = abc[abc_shift]
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
