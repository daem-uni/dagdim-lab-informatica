def calculate_subsidy(income, children_count):

    if 30_000 <= income < 40_000 and children_count >= 3:
        return 1000 * children_count
    elif 20_000 <= income < 30_000 and children_count >= 2:
        return 1500 * children_count
    elif income < 20_000:
        return 2000 * children_count

    return 0


income = float(input("Inserire il reddito annuo (-1 per uscire): "))

while income >= 0:
    children = int(input("Inserire il numero di figli: "))

    subsidy = round(calculate_subsidy(income, children), 2)
    if subsidy == 0:
        print("La famiglia non ha diritto ad un sussidio annuo.")
    else:
        print(f"La famiglia ha diritto a {subsidy}$ di sussidio annuo.")

    income = float(input("Inserire il reddito annuo (-1 per uscire): "))
