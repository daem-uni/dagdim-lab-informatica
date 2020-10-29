s = input("Inserire una stringa: ")

if s.isalpha():
    print("La stringa contiene solo lettere.")
if s.isupper():
    print("La stringa contiene solo lettere maiuscole.")
if s.islower():
    print("La stringa contiene solo lettere minuscole.")
if s.isdigit():
    print("La stringa contiene solo numeri.")
if s.isalnum():
    print("La stringa contiene solo lettere e numeri.")
if s[0].isupper():
    print("La stringa inizia con una lettera maiuscola.")
if s.endswith("."):
    print("La stringa termina con un punto.")