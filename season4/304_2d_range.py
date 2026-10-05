from typing import Dict, List, Optional, Set

def matrixPrint(mat: List[List[int]]):
    for row in mat:
        print(" ".join([(str(c) if str(c) != "" else "_") for c in row]))

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        self.mat = matrix

        self.mem = [[0 for _ in range(cols + 1)] for __ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                self.mem[r][c] = matrix[r - 1][c - 1]+self.mem[r - 1][c] \
                +self.mem[r][c - 1] -self.mem[r - 1][c - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.mem[row2 + 1][col2 + 1] - self.mem[row1][col2 + 1] - self.mem[row2 + 1][col1] + self.mem[row1][col1]


if __name__ == "__main__":
    o = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    matrixPrint(o.mat)
    print(o.sumRegion(1, 1, 2, 2))
