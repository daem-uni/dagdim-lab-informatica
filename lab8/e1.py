def merge(a, b):
    result = []
    
    if len(a) > len(b):
        lowest = len(b)
    else:
        lowest = len(a)


    for i in range(lowest):
        result.append(a[i])
        result.append(b[i])

    return result + a[lowest:] + b[lowest:]
