def reverse(array):
    for i in range(len(array) // 2):
        tmp = array[i]
        array[i] = array[-i - 1]
        array[-i - 1] = tmp

    return array