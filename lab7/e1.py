import random

array = []

for i in range(10):
   array.append(random.randint(0, 10000))

print("Indici pari: ", end="")
for i in range(0, len(array), 2):
    print(array[i], end=" ")
print()

print("Numeri pari: ", end="")
for element in array:
    if element % 2 == 0:
        print(element, end=" ")
print()


print("Al contrario: ", end="")
for i in range(len(array)-1, -1, -1):
    print(array[i], end=" ")
print()

print("Primo e ultimo:", array[0], array[-1])