word = input("Inserire una parola: ")

for i in range(len(word)+1):
    for j in range(len(word)+1-i):
        subword = word[j:j+i]

        if len(subword) > 0:
            print(subword)