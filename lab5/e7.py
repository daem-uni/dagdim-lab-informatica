MAX_TICKETS = 100

tickets_left = MAX_TICKETS
tickets_to_buy = 0
buyers = 0

while tickets_left > 0:
    tickets_to_buy = int(input("Inserire numero biglietti da acquistare: "))
    print("Acquisto avvenuto con successo!")
    tickets_left -= tickets_to_buy
    buyers += 1
    
    print(tickets_left, "biglietti rimasti.")
    print()
    
print("Biglietti esauriti. Acquirenti totali:", buyers)