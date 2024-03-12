def crypt(string, shift):
    str = ""
    for char in string:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            str += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            str += char
    return str


while True:

    prompt = str(input("Nachricht: "))
    prompt_offset = str(input("Offset: "))
    offset = 0
    prompt_direction = str(input("d for decrypt OR e for encrypt: "))

    if 'd' in prompt_direction:
        offset = int(prompt_offset)
    elif 'e' in prompt_direction:
        offset = -abs(int(prompt_offset))
    else:
        print("You fucked up!")
        exit()

    print(crypt(prompt, offset))


    
