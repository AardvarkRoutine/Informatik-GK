def straightIntersects(n):
    if n <= 1:
        return 0
    else:
        return straightIntersects(n-1) + n-1

n=int(input("Anzahl der Geraden: "))
print("Anzahl der Schnittpunkte: ", straightIntersects(n))