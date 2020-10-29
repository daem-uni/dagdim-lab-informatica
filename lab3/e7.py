amount = int(input("Inserire il reddito imponibile: "))
married = input("Sei coniugato? [y/N]: ") == "y"

if married:
    if amount > 64000:
        tax = 8800 + (amount - 64000) * .25
    elif amount > 16000:
        tax = 1600 + (amount - 16000) * .15
    else:
        tax = amount * .10
else:
    if amount > 32000:
        tax = 4400 + (amount - 32000) * .25
    elif amount > 8000:
        tax = 800 + (amount - 8000) * .15
    else:
        tax = amount * .10


print(f"Le tasse sono {tax:.2f}$")