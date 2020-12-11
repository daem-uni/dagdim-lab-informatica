files = input("Inserire la lista di file: ").split(", ")
word = input("Inserire la parola da cercare: ").lower()

for fileName in files:
    currentFile = open(fileName, 'r', encoding='utf8')

    for line in currentFile.readlines():
        if word in line.lower():
            print(f"{fileName}: {line.strip()}")

    currentFile.close()
