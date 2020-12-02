def removeMin(array):
    minIndex = 0
    for i in range(len(array)):
        if array[i] < array[minIndex]:
            minIndex = i
        
    return array[:minIndex] + array[minIndex + 1:]
