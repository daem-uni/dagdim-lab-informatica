def value(char):
    if char == "I":
        return 1
    elif char == "V":
        return 5
    elif char == "X":
        return 10
    elif char == "L":
        return 50
    elif char == "C":
        return 100
    elif char == "D":
        return 500
    elif char == "M":
        return 1000

    return 0


def roman_to_decimal(roman):
    total = 0

    while len(roman) > 0:
        if len(roman) > 1 and value(roman[0]) < value(roman[1]):
            total += value(roman[1]) - value(roman[0])
            roman = roman[2:]
        else:
            total += value(roman[0])
            roman = roman[1:]

    return total

roman_input = input("Inserisci un numero romano: ")
print("L'equivalente decimale è:", roman_to_decimal(roman_input))