import random

def main():
    while True:
        # Zahl zwischen 0 und 15 würfeln
        zufallszahl = random.randint(0, 15)

        # Ausgabe der gewürfelten Zahl
        print(f"Gewürfelte Zahl: {zufallszahl}")

        # Benutzer nach Wiederholung fragen
        wiederholen = input("Möchten Sie den Vorgang wiederholen? (ja/nein): ")

        # Überprüfen, ob der Benutzer "nein" eingegeben hat
        if wiederholen.lower() != 'ja':
            break  # Die Schleife verlassen, wenn der Benutzer nicht wiederholen möchte

if __name__ == "__main__":
    main()