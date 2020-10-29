mark = float(input("Inserire voto: "))

if mark < .35:
    print("F")
elif mark < .85:
    print("D-")
elif mark < 1.15:
    print("D")
elif mark < 1.50:
    print("D+")
elif mark < 1.85:
    print("C-")
elif mark < 2.15:
    print("C")
elif mark < 2.50:
    print("C+")
elif mark < 2.85:
    print("B-")
elif mark < 3.15:
    print("B")
elif mark < 3.50:
    print("B+")
elif mark < 3.85:
    print("A-")
elif mark < 4.15:
    print("A")
else:
    print("A+")
