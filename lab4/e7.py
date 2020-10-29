import random
import math

print("NIM")

balls = random.randint(10, 100)
ai_level = random.randint(0, 1)

print("Numero Biglie: ")


turn = random.randint(0, 1)
turn_num = 1

while balls > 0:
	print("Turno", turn_num)
	print("Biglie rimanenti:", balls)
	if turn == 0: # Player Turn
		pass
	else: # AI Turn
		print("Turno del computer.")

		if ai_level == 0: # dumb
			move = random.randint(1, math.floor(balls / 2))
		else: # Smart


	print()