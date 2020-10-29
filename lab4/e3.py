n = int(input("Inserisci un numero intero: "))

for i in range(n): # Square
	print("#" * n)

print("")

for i in range(n * 2 - 1):
	m = abs(n - (i + 1))
	print(" " * m + "#" * (2 * (n - m - 1) + 1) + " " * m)

