distanza = int(input("Inserire distanza: "))
contachilometriInizio = int(input("Inserire contachilometri inizio: "))
contachilometriFine = int(input("Inserire contachilometri fine: "))
giorniLavoro = int(input("Inserire numero di giorni di lavoro: "))

chilometriFatti = contachilometriFine - contachilometriInizio
chilometriLavoro = giorniLavoro * distanza * 2 # Conta andata e ritorno
propLavoro = chilometriLavoro / chilometriFatti
propNonLavoro = 1 - propLavoro

print("La percentuale di chilmetri per lavoro è:", propLavoro * 100, "%")
print("La percentuale di chilmetri non per lavoro è:", propNonLavoro * 100, "%")