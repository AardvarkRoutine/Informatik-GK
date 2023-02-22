def subPlanes(n):
    if n==1:
        return 2
    else:
        return subPlanes((n-1)+n)
print(subPlanes(int(input("Geben sie die Anzahl an Geraden an, die die Ebene schneiden: "))))