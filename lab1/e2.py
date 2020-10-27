conto = int(input("Inserisci conto: "))
numeroAmici = int(input("Inserisci il numero di amici: "))
proporzioneMancia = 15/100

contoTotale = conto * (proporzioneMancia + 1)
contoPerAmico = contoTotale / numeroAmici

print("Conto:", conto)
print("Conto Totale:", contoTotale)
print("Conto per amico:", contoPerAmico)