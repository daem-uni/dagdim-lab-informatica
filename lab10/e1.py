inputFile = open("input.txt", "r", encoding='utf8')
outputFile = open("output.txt", "w+", encoding='utf8')

i = 1

currentLine = inputFile.readline()
while currentLine:
    outputFile.write(f"/*{i}*/{currentLine}")
    currentLine = inputFile.readline()
    i = i + 1

inputFile.close()
outputFile.close()