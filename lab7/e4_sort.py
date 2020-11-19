def sameSet(a, b):
    return equals(sorted(stripDuplicates(a)), sorted(stripDuplicates(b)))

def equals(a, b):
    if len(a) != len(b):
        return False

    for i in range(len(a)):
        if a[i] != b[i]:
            return False

    return True

def stripDuplicates(l):
    new_list = []
    for e in l:
        if e not in new_list:
            new_list.append(e)
    
    return new_list
