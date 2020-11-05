CORRECT_PIN = "1234"
MAX_TRIES = 3

tries_left = MAX_TRIES
pin = input(f"Insert your pni ({tries_left} tries left): ")

while tries_left > 1 and pin != CORRECT_PIN:
    tries_left -= 1
    print("Your PIN is incorrect.")
    pin = input(f"Insert your pni ({tries_left} tries left): ")

if pin == CORRECT_PIN:
    print("Your PIN is correct")
else:
    print("Your bank card is blocked")