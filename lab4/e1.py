user_input = input("Inserire primo numero: ")
running_sum = 0
minimum = 1e9+5
maximum = -1e9+5
count = 0

last = ""
dupes = ""

while user_input != "":
	num = int(user_input)

	if num > maximum:
		maximum = num
	if num < minimum:
		minimum = num

	running_sum += num
	count += 1

	if user_input == last and last != "":
		dupes += user_input + " "
	last = user_input

	print("Somma Parziale:", running_sum)


	user_input = input("Inserisci un altro numero (ENTER per finire): ")

print()
print("Il minimo è:", minimum)
print("Il massimo è:", maximum)
if len(dupes) > 0:
	print("I numeri ripetuti sono:", dupes)
