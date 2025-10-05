from typing import Dict, List, Optional, Set


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        total = rows * cols

        newGrid = [[0 for i in range(len(grid[0]))] for _ in range(rows)]

        for i in range(total):
            shifted = (i - k) % total
            newGrid[int(i / cols)][i % cols] = grid[int(shifted / cols)][shifted % cols]

        return newGrid


if __name__ == "__main__":
    o = Solution()
    print(o.shiftGrid([[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], 4))
