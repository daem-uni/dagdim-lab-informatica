year = int(input("Inserire l'anno: "))

if year % 4 == 0 and (year <= 1582 or year % 100 != 0 or year % 400 == 0):
	print("L'anno è bisestile.")
else:
	print("L'anno non è bisestile.") 