inputFile = open("input.txt", "r", encoding='utf8')
outputFile = open("output.txt", "w+", encoding='utf8')

lines = inputFile.readlines()
for i in range(len(lines)):
    outputFile.write(lines[-i-1].strip() + "\n")

inputFile.close()
outputFile.close()