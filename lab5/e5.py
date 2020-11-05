A = 0.1
B = 0.01
C = 0.01
D = 0.00002

prey_old = 1000
pred_old = 20

generations = int(input("Inserisci il numero di generazioni da simulare: "))

print("La popolazione iniziale di prede è", prey_old)
print("La popolazione iniziale di predatori è", pred_old)

for t in range(generations):
    prey_new = prey_old * (1 + A - B * pred_old)
    pred_new = pred_old * (1 - C + D * prey_old)

    print()
    print("Generazione", t + 1)
    print("Numero di prede:", prey_new)
    print("Numero di predatori:", pred_new)

    prey_old = prey_new
    pred_old = pred_new

print("Simulazione finita.")