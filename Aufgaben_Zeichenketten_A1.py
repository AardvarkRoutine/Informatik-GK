user_in = str(input("Bitte geben Sie eine Zeichenkette ein!\n"))
to_replace = str(input("Bitte geben Sie ein Zeichen oder eine Zeichenkette ein, welche ersetzt werden soll!\n"))
replace_with = str(input("Bitte geben sie ein zeichen oder eine Zeichenkette ein, womit die zu Ersetzenden Zeichen ersetzt werden sollen!\n"))
user_in = user_in.lower()
to_replace = to_replace.lower()
replace_with = replace_with.lower()
if to_replace in user_in:
    user_in = user_in.replace(to_replace, replace_with)
print(user_in)