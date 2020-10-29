n1 = int(input("Inserire primo numero: "))
n2 = int(input("Inserire secondo numero: "))
n3 = int(input("Inserire terzo numero: "))

if n1 < n2 and n2 < n3:
    print("increasing")
elif n1 > n2 and n2 > n3:
    print("decreasing")
else:
    print("neither")