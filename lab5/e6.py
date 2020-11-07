nation = input("Inserisci nazione (In francese): ")

article = "le "

if nation == "Etats-Unis" or nation == "Pays-Bas":
    article = "les "
elif nation[0].lower() in "aeiou":
    article = "l'"
elif nation not in ["Belize", "Cambodge", "Mexique", "Mozambique", "Zaïre", "Zimbabwe"] and nation[-1] == "e":
    article = "la "

print(article + nation)
