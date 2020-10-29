string = input("Inserisci stringa: ")

print("Stringa al contrario: ", end="")

for i in range(len(string)):
	print(string[len(string) - i - 1], end="")

print()