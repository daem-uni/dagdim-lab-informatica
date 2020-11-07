MAX_TICKETS = 100

tickets_left = MAX_TICKETS
tickets_to_buy = 0
buyers = 0

while tickets_left > 0:
    tickets_to_buy = int(input("Inserire numero biglietti da acquistare (Massimo 4): "))    
    while tickets_to_buy < 1 or tickets_to_buy > 4:
        print("Numero Invalido. Dev'essere minimo 1 e massimo 4.")
        tickets_to_buy = int(input("Inserire numero biglietti da acquistare (Massimo 4): "))    
        
    print("Acquisto avvenuto con successo!")
    tickets_left -= tickets_to_buy
    buyers += 1
    
    print(tickets_left, "biglietti rimasti.")
    print()

    tickets_to_buy = 0
    
print("Biglietti esauriti. Acquirenti totali:", buyers)