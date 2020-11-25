def mergeSorted(a, b):
    res = []

    ia = 0
    ib = 0

    while ia < len(a) and ib < len(b):
        if a[ia] < b[ib]:
            res.append(a[ia])
            ia += 1
        else:
            res.append(b[ib])
            ib += 1
    
    return res + a[ia:] + b[ib:]
