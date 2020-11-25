def neighborAverage(values, row, column):
    height = len(values)
    width = len(values[0])

    vals = [values[column][row]]

    if row > 0:
        vals.append(values[column][row - 1])
    if row < width - 1:
        vals.append(values[column][row + 1])
    
    if column > 0:
        vals.append(values[column - 1][row])
    if column < height - 1:
        vals.append(values[column + 1][row])

    if row > 0 and column > 0:
        vals.append(values[column - 1][row - 1])
    if row > 0 and column < height - 1:
        vals.append(values[column + 1][row - 1])
    
    if row < width - 1 and column > 0:
        vals.append(values[column - 1][row + 1])
    if row < width - 1 and column < height - 1:
        vals.append(values[column + 1][row + 1])

    print((row, column))
    print(vals)

    return sum(vals) / len(vals)

testMat = [
    [1, 2, 1],
    [2, 1, 2],
    [1, 2, 1]
]

resMat = []

for i in range(3):
    resMat.append([])
    for j in range(3):
        resMat[i].append(neighborAverage(testMat, i, j))

print(resMat)