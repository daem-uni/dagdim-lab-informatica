def sameSet(a, b):
    a_copy = list(a)
    b_copy = list(b)

    i = len(a_copy) - 1

    while i >= 0:
        remove = a_copy[i]

        (a_copy, flag) = remove_all(a_copy, remove)
        (b_copy, flag) = remove_all(b_copy, remove)

        if flag == False:
            return False

        while i > len(a_copy) - 1:
            i -= 1

    return len(b_copy) == 0

def remove_all(array, item):
    new_list = []
    flag = False
    for e in array:
        if e != item:
            new_list.append(e)
        else:
            flag = True

    return (new_list, flag)


print(sameSet([1, 4, 9, 16, 9, 7, 4, 9, 11], [11, 11, 7, 9, 16, 4, 1]))