def StraightsIntersects(n):
    print("Entering StraightsIntersects with n = " + str(n))
    if n == 1:
        return 0
    else:
        result = (n - 1) * (n - 2) // 2 + StraightsIntersects(n - 1)
        print("Returning " + str(result) + " from StraightsIntersects with n = " + str(n))
        return result

# Beispielaufrufe
#print(calculate_x(1)) # Erwartete Ausgabe: 0
#print(calculate_x(2)) # Erwartete Ausgabe: 1
#print(calculate_x(3)) # Erwartete Ausgabe: 3
#print(calculate_x(4)) # Erwartete Ausgabe: 6
#print(calculate_x(5)) # Erwartete Ausgabe: 10
#print(calculate_x(6)) # Erwartete Ausgabe: 15
#n = int(input("Enter a number: \n"))
n = int(input("Enter a number: \n"))
print(StraightsIntersects(n))