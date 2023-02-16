def recursive_sum(n):
    if n == 0:  # base case
        return 0
    else:
        return (n - 1) + n + recursive_sum(n - 1)
n = input("Enter a number: ")
n = int(n)
print(recursive_sum(n))