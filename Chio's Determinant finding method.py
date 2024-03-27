from typing import List, Tuple

class matrix:
    def __init__(self, matrix, val=0):
        if isinstance(matrix, List):
            self.matrix = matrix
        elif isinstance(matrix, Tuple):
            tempMatrix = []
            row, col = matrix
            for rowIter in range(row):
                tempMatrix.append([])
                for colIter in range(col):
                    tempMatrix[rowIter].append(val)
            self.matrix = tempMatrix
        else:
            raise ValueError

    def __getitem__(self, locationTuple):
        return self.matrix[locationTuple]

    def __add__(self, other):
        if self.size() == other.size():
            resultMatrix = matrix(self.size())
            for rowIter in range(self.size()[0]):
                for colIter in range(self.size()[1]):
                    resultMatrix.matrix[rowIter][colIter] = self.matrix[rowIter][colIter] + other.matrix[rowIter][
                        colIter]
            return resultMatrix
        else:
            raise ValueError

    def __mul__(self, other):
        if self.size()[1] == other.size()[0]:
            resultMatrix = matrix((self.size()[0], other.size()[1]))

            for rowIter in range(resultMatrix.size()[0]):
                for colIter in range(resultMatrix.size()[1]):
                    row = []
                    row = self[rowIter].copy()

                    col = []
                    for i in range(other.size()[0]):
                        col.append(other[i][colIter])

                    rowTimesCol = []
                    for j in range(len(row)):
                        rowTimesCol.append(row[j] * col[j])

                    resultMatrix[rowIter][colIter] = sum(rowTimesCol)

            return resultMatrix
        else:
            raise ValueError

    def __str__(self):
        tempString = ''
        for rowIter in range(self.size()[0]):
            tempString += '| '
            for colIter in range(self.size()[1]):
                tempString += str("{0:2d}".format(self[rowIter][colIter])) + ' '
            tempString += '|'
            if rowIter != self.size()[0] - 1:
                tempString += '\n'
        return tempString

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

def chio(m):
    if m.size()[0] == 2 and m.size()[1] == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    elif m.size()[0] > 2 and m.size()[1] > 2:
        changeSignFlag = False
        if m[0][0] == 0:

            tempMatrixList = []

            for rIt in range(m.size()[0]):
                tempMatrixList.append(m[rIt])
                if m[rIt][0] != 0:
                    goodRowIndex = rIt

            if goodRowIndex is None:
                raise ValueError

            tempMatrixList[0], tempMatrixList[goodRowIndex] = tempMatrixList[goodRowIndex], tempMatrixList[0]

            m = matrix(tempMatrixList)

            changeSignFlag = True

        resultMatrix = matrix((m.size()[0] - 1, m.size()[1] - 1))
        for rowIter in range(resultMatrix.size()[0]):
            for colIter in range(resultMatrix.size()[1]):
                resultMatrix[rowIter][colIter] = chio(
                    matrix([[m[0][0], m[0][rowIter + 1]], [m[colIter + 1][0], m[colIter + 1][rowIter + 1]]]))

        det = (1 / (m[0][0] ** (m.size()[0] - 2))) * chio(resultMatrix)
        if changeSignFlag:
            det *= -1
        return det
    else:
        raise ValueError


test = matrix([[5, 1, 1, 2, 3], [4, 2, 1, 7, 3], [2, 1, 2, 4, 7], [9, 1, 0, 7, 0], [1, 4, 7, 2, 2]])
test2 = matrix([[0, 1, 1, 2, 3], [4, 2, 1, 7, 3], [2, 1, 2, 4, 7], [9, 1, 0, 7, 0], [1, 4, 7, 2, 2]])

print(chio(test))
print(chio(test2))