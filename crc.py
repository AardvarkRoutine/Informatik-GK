# -*- coding: utf8 -*-

def crc(bitfolge, polynom = '10011'):
    """
    zu der 'nachricht' und zu dem 'polynom' (Strings aus 0 und 1) wird
    die CRC-'PrÃ¼fsumme' berechnet (String aus 0 und 1)
    """
    lp = len(polynom)
    ln = len(bitfolge)
    for j in range(lp-1):
        bitfolge = bitfolge+'0'
    bitliste = list(bitfolge)
    schieberegister = bitliste[:lp]
    for i in range(ln):
        if schieberegister[0] == '1':
            for j in range(lp):
                if schieberegister[j] == polynom[j]:
                    schieberegister[j] = '0'
                else:
                    schieberegister[j] = '1'
        if i < ln-1:
            schieberegister = schieberegister[1:lp]+list(bitliste[lp+i])
    return ''.join(schieberegister[1:])


from random import random
def bitfolgeManipulieren(bitfolge, fehlerwahrscheinlichkeit):
    bitfolgeNeu = ''
    for bit in bitfolge:
        zufallszahl = random()
        if zufallszahl < fehlerwahrscheinlichkeit:
            if bit == '0':
                bitNeu = '1'
            else:
                bitNeu = '0'
        else:
            bitNeu = bit
        bitfolgeNeu = bitfolgeNeu + bitNeu
    return bitfolgeNeu
            


# Test
fehlerwahrscheinlichkeit = 0.5
bitfolge = '01101010'
zusatzbits = crc(bitfolge)
bitfolgeErweitert = bitfolge + zusatzbits
print(bitfolgeErweitert)
bitfolgeErweitertManipuliert = bitfolgeManipulieren(bitfolgeErweitert, fehlerwahrscheinlichkeit)
print(bitfolgeErweitertManipuliert)
bitfolgeNeu = bitfolgeErweitertManipuliert[0:8]
zusatzbitsNeu = bitfolgeErweitertManipuliert[8:12]
if crc(bitfolgeNeu) == zusatzbitsNeu:
    print('kein Fehler erkannt')
else:
    print('Fehler erkannt')