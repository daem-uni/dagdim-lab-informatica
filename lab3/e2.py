mark = input("Inserire voto: ")

if mark.startswith("A"):
	numeric_mark = 4
elif mark.startswith("B"):
	numeric_mark = 3
elif mark.startswith("C"):
	numeric_mark = 2
elif mark.startswith("D"):
	numeric_mark = 1
elif mark.startswith("F"):
	numeric_mark = 0

if mark.endswith("+"):
	numeric_mark += .3
elif mark.endswith("-"):
	numeric_mark -= .3

print("Il voto è", numeric_mark)