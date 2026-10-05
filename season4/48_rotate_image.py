
from typing import List, Set, Dict, Optional

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # rotate clockwise can also be achieved by mirroring main axis
        # then flip on the vertical axis

        # main axis flip
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                if r < c:
                    temp = matrix[c][r]
                    matrix[c][r]  = matrix[r][c]
                    matrix[r][c] = temp

        for row in matrix:
            row.reverse()
        


if __name__ == "__main__":
    mat =  [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    o = Solution()
    o.rotate(mat)
    print(mat)