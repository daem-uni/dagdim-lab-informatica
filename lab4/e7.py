import random
import math

balls = random.randint(10, 100)
ai_level = random.randint(0, 1)
turn = random.randint(0, 1)

print("Numero Biglie:", balls)
if ai_level == 0:
    print("Strategia AI: Casuale")
else:
    print("Strategia AI: Ottimale")

input("Premi invio per iniziare: ")

print()

if turn == 0:
    print("Inizia il giocatore!")
else:
    print("Inizia la AI!")


turn_num = 1

while balls > 0:
    max_move = math.ceil(balls / 2)
    print("Turno", turn_num)
    print("Biglie rimanenti:", balls)
    print("Mossa massima:", max_move)

    if turn == 0: # Player Turn
        move = int(input(f"Inserisci il numero di biglie (Tra 1 e {max_move}): "))
        while move > max_move or move < 0:
            print("Numero invalido.")
            move = int(input((f"Inserisci il numero di biglie (Tra 1 e {max_move}): ")))

    else: # AI Turn
        if ai_level == 0: # dumb
            move = random.randint(1, max_move)
        else: # Smart
            nearest_power = int(2 ** math.floor(math.log2(balls))) - 1
            distance = balls - nearest_power

            if distance > 0:
                move = distance
            else:
                move = random.randint(1, max_move)

        print("Turno del computer...")
        print(f"Prende {move} biglie!")

    balls -= move
    if balls > 0:
        turn_num += 1
        if turn == 1:
            turn = 0
        else:
            turn = 1
    print()

print("Partita finita! Il vincitore è ", end="")
if turn == 1:
    print("il giocatore!")
else:
    print("il computer!")