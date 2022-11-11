txt = "Montag"
ntxt=""
ntxt += txt[5]
ntxt += txt[4]
ntxt += txt[3]
ntxt += txt[2]
ntxt += txt[1]
ntxt += txt[0]
print(ntxt)

# Das allgemeine Umkehrproblem ist noch nicht gelöst, da das Programm nur für das spezifische Wort "Montag" funktionert und
# praktisch keine Anwendbarkeit hat

user_in = str(input("Bitte geben sie eine zu reversierende Zeichenkette ein!\n"))
user_in = user_in[::-1]
print(user_in)