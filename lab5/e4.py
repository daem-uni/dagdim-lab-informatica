RANDOM_NUMS_TO_GENERATE = 100

a = 32310901
b = 1729
m = 2 ** 24

r = int(input("Inserisci il seed: "))

for i in range(RANDOM_NUMS_TO_GENERATE):
    r = (a * r + b) % m
    print(r)