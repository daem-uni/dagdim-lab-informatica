from math import sqrt

def isMagicSquare(matrix):
    magicSum = sum(matrix[0])

    for i in range(len(matrix)):
        if sum(matrix[i]) != magicSum:
            return False
    
    for i in range(len(matrix)):
        colSum = 0
        for j in range(len(matrix)):
            colSum += matrix[j][i]

        if colSum != magicSum:
            return False

    mainDiagSum = 0
    secDiagSum = 0
    for i in range(len(matrix)):
        mainDiagSum += matrix[i][i]
        secDiagSum += matrix[i][-i - 1]
    
    if mainDiagSum != magicSum or secDiagSum != magicSum:
        return False

    return True

def matrixify(values):
    side = int(sqrt(len(values)))
    result = []
    
    for i in range(side):
        result.append([])
        for j in range(side):
            result[i].append(values[i * side + j])
    return result
    
def checkFromList(numbers):
    for i in range(max(numbers)):
        if (i + 1) not in numbers:
            return False

    return isMagicSquare(matrixify(values))


# values = [16, 3, 2, 13, 5, 10, 11, 8, 9, 6, 7, 12, 4, 15, 14, 1]

values = []
print("Inserire sedici numeri:")
for i in range(16):
    values.append(int(input(f"({16 - i} rimasti): ")))

if checkFromList(values):
    print("I valori formano un quadrato magico.")
else:
    print("I valori non formano un quadrato magico.")