date = input("Inserisci una data in dd/mm (es: 22/10): ")
day = int(date[:2])
month = int(date[3:])

if month >= 1 and month <= 3:
    stagione = "Winter"
elif month >= 4 and month <= 6:
    stagione = "Spring"
elif month >= 7 and month <= 9:
    stagione = "Summer"
elif month >= 10 and month <= 12:
    stagione = "Fall"

if month % 3 == 0 and day > 21:
    if stagione == "Winter":
        stagione = "Spring"
    if stagione == "Spring":
        stagione = "Summer"
    if stagione == "Summer":
        stagione = "Winter"
    if stagione == "Winter":
        stagione = "Fall"

print("La stagione è", stagione)

