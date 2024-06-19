from typing import Dict, List, Optional, Set


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        cols = len(matrix[0])
        rows = len(matrix)
        self.cache = [[0 for _ in range(cols)] for __ in range(rows)]
        if not matrix:
            return
        lastSum = 0

        # calc sum of first row and col
        firstRow = matrix[0]
        for i in range(cols):
            lastSum += firstRow[i]
            self.cache[0][i] = lastSum

        lastSum = 0
        for i in range(rows):
            lastSum += matrix[i][0]
            self.cache[i][0] = lastSum

        for i in range(1, rows):
            for j in range(1, cols):
                self.cache[i][j] = self.cache[i - 1][j] + self.cache[i][j - 1] + matrix[i][j] - self.cache[i - 1][j - 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        val = self.cache[row2][col2]
        if col1 > 0:
            val -= self.cache[row2][col1 - 1]
        if row1 > 0:
            val -= self.cache[row1 - 1][col2]
        if row1 > 0 and col1 > 0:
            val += self.cache[row1 -1][col1 - 1]
        return val


if __name__ == "__main__":
    o = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(o.sumRegion(2, 1, 4, 3))
