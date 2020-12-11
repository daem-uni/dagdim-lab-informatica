ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def stripDuplicates(string):
    unique = []
    resString = ""
    for l in string:
        if l not in unique:
            unique.append(l)
            resString += l

    return resString

def createEncryptionString(key):
    result = ALPHABET
    newKey = stripDuplicates(key.upper())
    for s in newKey:
        result = result.replace(s, '')
    return newKey + result[::-1]

def encrypt(char, encString):
    if char in ALPHABET:
        return encString[ALPHABET.index(char)]
    elif char.upper() in ALPHABET:
        return encString[ALPHABET.index(char.upper())].lower()
    else:
        return char

def decrypt(char, encString):
    if char in encString:
        return ALPHABET[encString.index(char)]
    elif char.upper() in encString:
        return ALPHABET[encString.index(char.upper())].lower()
    else:
        return char



isEncrypt = input("Inserisci 1 per criptare, o 2 per decrittare: ") == "1"
# fileName = input("Inserisci il nome del file: ")
key = input("Inserisci la chiave: ")
encString = createEncryptionString(key)

with open("encrypted.txt", "r") as inFile:
    with open("output.txt", "w+") as outFile:
        char = inFile.read(1)
        while char != "":
            if isEncrypt:
                outFile.write(encrypt(char, encString))
            else:
                outFile.write(decrypt(char, encString))
            char = inFile.read(1)

