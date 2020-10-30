string = input("Inserire una stringa: ")


print("Le maiuscole sono: ", end="")

for letter in string:
    if letter.isupper():
        print(letter, end="")
print()

print("Stringa alterna: ", end="")
for i in range(0, len(string), 2):
    print(string[i], end="")
print()

print("Senza vocali: ", end="")
for letter in string:
    if letter.lower() in "aeiou":
        print("_", end="")
    else:
        print(letter, end="")
print()


digits = 0
for letter in string:
    if letter.isdigit():
        digits += 1
print("Numero Cifre:", digits)

print("Posizioni vocali: ", end="")
for i in range(len(string)):
    if string[i] in "aeiou":
        print(i, end=" ")
print()
