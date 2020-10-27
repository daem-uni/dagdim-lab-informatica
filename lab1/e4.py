mese = int(input("Inserisci il mese: "))
giorno = int(input("Inserisci il giorno: "))

if mese in [1,2,3]:
	stagione = "Winter"
elif mese in [4,5,6]:
	stagione = "Spring"
elif mese in [7,8,9]:
	stagione = "Summer"
elif mese in [10,11,12]:
	stagione = "Fall"

if mese % 3 == 0 and giorno >= 21:
	if stagione == "Winter":
		stagione = "Spring"
	elif stagione == "Spring":
		stagione = "Summer"
	elif stagione == "Summer":
		stagione = "Fall"
	else:
		stagione = "Winter"
print(stagione)