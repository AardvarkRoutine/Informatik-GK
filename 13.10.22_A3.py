import math as m
list = []
for i in range(1, 100 +1):
    if m.sqrt(i) % 2 == 0:
        list.append(i)
print(list)