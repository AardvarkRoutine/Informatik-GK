def ggt(n1, n2):
    if n1 != n2:
        if n1 > n2:
            return ggt(n1 % n2, n2)
        else:
            return ggt(n1, n2 % n1)
    else:
        if n1==1:
            return "Es existiert kein ggT"
        else:
            return n1
print(ggt(int(input("Zahl 1: ")), int(input("Zahl 2: "))))