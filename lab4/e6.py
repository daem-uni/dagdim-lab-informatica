word = input("Inserire una parola: ")

for length in range(len(word) + 1):
    for start in range(len(word) + 1 - length):
        subword = word[start:start + length]

        if len(subword) > 0:
            print(subword)