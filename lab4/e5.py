import math

n = int(input("Inserire un numero: "))

for i in range(2, n + 1): # Parte da 2, perché 1 non è primo.
    prime = True

    if i != 2 and i != 3: # 2 o 3 sono numeri primi che non verrebbero contati da questo algoritmo
        # Basta controllare fino a sqrt(i) perché, se ci fosse un numero maggiore di 
        # sqrt(i) che divide i, allora necessariamente ci dovrebbe essere un altro numero
        # minore di sqrt(i) che divide i, e questo numero lo avremmo già trovato.
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                prime = False

    if prime:
        print(i)
