n = int(input("Inserire un numero: "))

for i in range(2, n + 1):
    prime = True

    if i != 2 and i != 3:
        for j in range(2, int(i ** .5) + 1):
            if i % j == 0:
                prime = False

    if prime:
        print(i)