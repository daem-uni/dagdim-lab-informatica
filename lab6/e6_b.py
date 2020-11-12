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
    if len(roman) == "":
        return 0
    
    if len(roman) > 1 and value(roman[0]) < value(roman[1]):
        if len(roman) == 2:
            return value(roman[1]) - value(roman[0])
        else:
            return value(roman[1]) - value(roman[0]) + roman_to_decimal(roman[2:])
    else:
        if len(roman) == 1:
            return value(roman)
        else:
            return value(roman[0]) + roman_to_decimal(roman[1:])

roman_input = input("Inserisci un numero romano: ")
print("L'equivalente decimale è:", roman_to_decimal(roman_input))
