N = int(input("Enter a Number that you want the factorial of: "))
def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N-1)
print("The factorial of", N, "is", factorial(N))
