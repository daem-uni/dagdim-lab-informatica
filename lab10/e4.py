types = []
sums = []

try:
    with open('hoteldata.txt', 'r', encoding='utf8') as inFile:
        line = inFile.readline()
        while line != "":
            currentDayData = line.split(';')
            if len(currentDayData) != 4:
                raise Exception("Invalid Format")
            
            if currentDayData[1] not in types:
                types.append(currentDayData[1])
                sums.append(float(currentDayData[2]))
            else:
                sums[types.index(currentDayData[1])] += float(currentDayData[2])            

            line = inFile.readline()

        for i in range(len(types)):
            print(f"L'importo totale per i servizi di tipo {types[i]} è: ${round(sums[i], 2)}")
except FileExistsError:
    print("File non esistente")
except Exception as e:
    print("Formato invalido")
    