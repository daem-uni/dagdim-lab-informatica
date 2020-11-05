n = int(input("Inserisci il numero da fattorizzare: "))

while n != 1:
    factor = 2
    while n % factor != 0:
        factor += 1

    n = n // factor
    print(factor)
    