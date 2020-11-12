def countWords(string):
    word_count = 1
    for letter in string:
        if letter == " ":
            word_count += 1

    return word_count

