prices = [
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
    [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
    [30, 40, 50, 50, 50, 50, 50, 50, 40, 30],
]

buyMode = input("Inserire 1 per scegliere per prezzo, 2 per scegliere per posto. Premere INVIO per chiudere il programma: ")

while buyMode != "":
    if buyMode == "1":
        availablePrices = []
        for row in prices:
            for e in row:
                if str(e) not in availablePrices:
                    availablePrices.append(str(e))

        price = int(input(f"Inserire prezzo (Uno di {', '.join(availablePrices)}): "))
        while str(price) not in availablePrices:
            print("Prezzo non valido.")
            price = int(input(f"Inserire prezzo (Uno di {', '.join(availablePrices)}): "))
        
        seatFound = False
        for y in range(len(prices)):
            for x in range(len(prices[y])):
                if not seatFound and prices[y][x] == price:
                    print(f"Ti è stato assegnato il posto in colonna {y + 1} e riga {x + 1}")
                    prices[y][x] = 0
                    seatFound = True
        
        if not seatFound:
            print("I posti con quel prezzo sono finiti.")
    elif buyMode == "2":
        row = int(input("Inserire colonna: "))
        col = int(input("Inserire riga: "))

        while col < 0 or col >= len(prices) or row < 0 or col >= len(prices[0]) or prices[col][row] == 0:
            print("Posto non valido.")
            row = int(input("Inserire colonna: "))
            col = int(input("Inserire riga: "))

        print(f"Posto preso! È costato {prices[col][row]} euro.")
        prices[col][row] = 0

    buyMode = input("Inserire 1 per scegliere per prezzo, 2 per scegliere per posto, 0 per chiudere il programma: ")
