def countVowels(string):
    count = 0
    for letter in string:
        if letter.lower() in "aeiou":
            count += 1
    return count

