A = float(input("Inserire il valore A: ")) # 0.1
B = float(input("Inserire il valore B: ")) # 0.01
C = float(input("Inserire il valore C: ")) # 0.01
D = float(input("Inserire il valore D: ")) # 0.00002

prey_old = int(input("Inserire il valore di prede iniziali: ")) # 1000
pred_old = int(input("Inserire il numero di predatori iniziale: ")) # 20

generations = int(input("Inserisci il numero di generazioni da simulare: "))

print("La popolazione iniziale di prede è", prey_old)
print("La popolazione iniziale di predatori è", pred_old)

for t in range(generations):
    prey_new = int(prey_old * (1 + A - B * pred_old))
    pred_new = int(pred_old * (1 - C + D * prey_old))

    print()
    print("Generazione", t + 1)
    print("Numero di prede:", prey_new)
    print("Numero di predatori:", pred_new)

    prey_old = prey_new
    pred_old = pred_new

print("Simulazione finita.")