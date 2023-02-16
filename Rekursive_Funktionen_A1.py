def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
x = int(input("Enter a number x:\n"))
n = int(input("Enter a power n:\n"))
print("Ergebnis:\n", power(x, n))