s1 = input("Inserisci la prima stringa: ")
s2 = input("Inserisci la seconda stringa: ")
s3 = input("Inserisci la terza stringa: ")

if s1 < s2:
    if s2 < s3:
        print(s1, s2, s3)
    else:
        if s3 < s1:
            print(s3, s1, s2)
        else:
            print(s1, s3, s2)
else:
    if s3 < s2:
        print(s3, s2, s1)
    else:
        if s1 < s3:
            print(s2, s1, s3)
        else:
            print(s2, s3, s1)
