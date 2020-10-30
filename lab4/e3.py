n = int(input("Inserisci un numero intero: "))

# Quadrato
for i in range(n):
    print("*" * n)
print()

# Rombo
for i in range(n * 2 - 1): # Rombo
    # Numero Spazi
    # Va da n - 1 a 0, e poi da 0 a n - 1.
    spaces_num = abs(n - (i + 1))

    # Numero Asterischi
    # Segue la formula 2k + 1, perché sono sempre dispari
    # Va al contrario rispetto a spaces_num, parte da 1, arriva a
    # 2n - 1 e poi torna a 1.
    stars_num = 2 * (n - spaces_num - 1) + 1
    print(" " * spaces_num + "*" * stars_num  + " " * spaces_num)

