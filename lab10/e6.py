from math import sqrt

ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

def printMatrix(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            print(f"{matrix[y][x]:<2}", end="")
        print()

def stripDuplicates(string):
    unique = []
    resString = ""
    for l in string:
        if l not in unique:
            unique.append(l)
            resString += l

    return resString

def stringToMatrix(string):
    side = int(sqrt(len(string)))
    resMatrix = []

    for y in range(side):
        resMatrix.append([])
        for x in range(side):
            resMatrix[y].append(string[x + y * side])
    
    return resMatrix

def createEncryptionString(key):
    result = ALPHABET
    newKey = stripDuplicates(key.upper()).replace("J", "I")
    for s in newKey:
        result = result.replace(s, '')
    return newKey + result

def findInMatrix(element, matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == element:
                return (r, c)

def playfairEncryptPair(pair, encMat):
    isfirstLower = pair[0].islower()
    isSecondLower = pair[1].islower()

    pos1 = findInMatrix(pair[0].upper(), encMat)
    pos2 = findInMatrix(pair[1].upper(), encMat)

    if pos1 == pos2:
        return pair
    if pos1[0] == pos2[0] or pos1[1] == pos2[1]:
        return pair[::-1]

    letter1 = encMat[pos1[0]][pos2[1]]
    letter2 = encMat[pos2[0]][pos1[1]]
    
    if isfirstLower:
        letter1 = letter1.lower()
    if isSecondLower:
        letter2 = letter2.lower()

    return letter1 + letter2

def playfairEncryptMessage(message, key):
    # Creo la stringa e la tabella di criptaggio
    encString = createEncryptionString(key)
    encMat = stringToMatrix(encString)

    # Sostituisco le j con le i
    message = message.replace('j', 'i').replace('J', 'I')

    # Divido il messaggio in coppie di due lettere
    splitMessage = []
    lastLetter = ""
    for letter in message:
        # Se la lettera non è nel cifrario, non la metto in una coppia.
        # Così che nel messaggio finale rimarrà intatta
        if letter.upper() not in encString:
            if lastLetter != "":
                # Aggiungo una X per finire la coppia in caso di uno spazio
                if lastLetter.isupper():
                    splitMessage.append(lastLetter + "X")
                else:
                    splitMessage.append(lastLetter + "x")
                lastLetter = ""
            
            splitMessage.append(letter)
        else:
            if lastLetter == "":
                # Se non c'è una lastLetter, è l'inizio di una coppia
                lastLetter = letter
            else:
                # Altrimenti, fine della coppia
                if letter == lastLetter:
                    # Aggiungo una X tra una doppia e l'altra, per rendere
                    # più difficile decriptare il cifrario
                    if lastLetter.isupper():
                        splitMessage.append(lastLetter + "X")
                    else:
                        splitMessage.append(lastLetter + "x")
                    lastLetter = letter
                else:
                    splitMessage.append(lastLetter + letter)
                    lastLetter = ""

    if lastLetter != "":
        # Se le lettere sono dispari, finisco le lettere con una X
        if lastLetter.isupper():
            splitMessage.append(lastLetter + "X")
        else:
            splitMessage.append(lastLetter + "x")
    
    # Creo la stringa finale
    resultString = ""
    for pair in splitMessage:
        if len(pair) != 2:
            # Se pair non è una coppia, è un carattere speciale che va lasciato così
            resultString += pair
        else:
            # Altrimenti, cripto la coppia
            resultString += playfairEncryptPair(pair, encMat)

    return resultString

inputFileName = input("Inserisci il nome del file da criptare/decriptare: ")
outputFileName = input("Inserisci il nome del file su cui salvare il messaggio (O premi invio per stamparlo a schermo): ")
key = input("Inserisci la chiave: ")


with open(inputFileName, 'r', encoding='utf8') as inputFile:
    message = inputFile.read()

if outputFileName != '':
    with open(outputFileName, 'w+', encoding='utf8') as outputFile:
        outputFile.write(playfairEncryptMessage(message, key))
else:
    print(playfairEncryptMessage(message, key))
