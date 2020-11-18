def sameSet(a, b):
    a_new = stripDuplicates(a)
    b_new = stripDuplicates(b)

    if len(a_new) != len(b_new):
        return False

    for e in a_new:
        if e not in b_new:
            return False
    
    return True

def stripDuplicates(l):
    new_list = []
    for e in l:
        if e not in new_list:
            new_list.append(e)
    
    return new_list
