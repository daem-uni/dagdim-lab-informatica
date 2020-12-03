def swapFirstAndLast(array):
    tmp = array[-1]
    array[-1] = array[0]
    array[0] = tmp

    return array

def rightShift(array):
    tmp = array[-1]
    for i in range(len(array)-1, 0, -1):
        array[i] = array[i-1]
    array[0] = tmp

    return array

def subEvenWithZero(array):
    for i in range(len(array)):
        if array[i] % 2 == 0:
            array[i] = 0
    
    return array

def subWithNeighbouringGreater(array):
    newArr = [array[0]]
    for i in range(1, len(array)-1):
        newArr.append(max(array[i-1], array[i+1]))
    newArr.append(array[-1])

    return newArr

def removeCenterElement(array):
    if len(array) % 2 == 1:
        return array[:len(array)//2] + array[len(array)//2 + 1:]
    else:
        return array[:len(array)//2-1] + array[len(array)//2 + 1:]
    
def moveEvenToHead(array):
    evens = []
    odds = []

    for e in array:
        if e % 2 == 0:
            evens.append(e)
        else:
            odds.append(e)

        return evens + odds

def secondMax(array):
    array.remove(max(array))
    return max(array)

def isOrderedIncreasing(array):
    last = array[0]
    for e in array:
        if last < e:
            return False

        last = e

    return True

def hasAdjacentDuplicates(array):
    last = array[0]
    for e in array[1:]:
        if last == e:
            return True

        last = e

    return False

def hasDuplicates(array):
    duplList = []
    for e in array:
        if e in duplList:
            return True
        else:
            duplList.append(e)
    
    return False


ex = int("Inserire punto dell'esercizio: ")

testArray = [1, 2, 3, 4, 5, 6]

print("Lista di test:", testArray)

if ex == 'a':
    print(swapFirstAndLast(testArray))
if ex == 'b':
    print(rightShift(testArray))
if ex == 'c':
    print(subEvenWithZero(testArray))
if ex == 'd':
    print(subWithNeighbouringGreater(testArray))
if ex == 'e':
    print(removeCenterElement(testArray))
if ex == 'f':
    print(moveEvenToHead(testArray))
if ex == 'g':
    print(secondMax(testArray))
if ex == 'h':
    print(isOrderedIncreasing(testArray))
if ex == 'i':
    print(hasAdjacentDuplicates(testArray))
if ex == 'j':
    print(hasDuplicates(testArray))