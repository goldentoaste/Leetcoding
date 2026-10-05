from typing import Dict, List, Optional, Set

null = None


class Solution:
    def maximalRectangle(self, mat):
        """
        Observe each position can be end of a rect, at this position, width of the rect can be gotten
        instantly by precomputing a prefix sum array.

        Then from that position all rects that has that width can be checked.

        Overall O(N^3) time, O(N^2) space
        """

        maxArea = 0
        mem = [[0] * len(mat[0]) for _ in range(len(mat))]
        for r, row in enumerate(mat):
            for c, num in enumerate(row):
                num = int(num)
                if num != 0:
                    mem[r][c] = num + (mem[r][c - 1] if c > 0 else 0)

        for r, row in enumerate(mem):
            for c, width in enumerate(row):
                if width == 0:
                    continue

                _r = r
                while _r > -1 and mem[_r][c] > 0:  # if width has decreased, this position is not the corner
                    width = min(width, mem[_r][c])
                    area = (r - _r + 1) * width
                    maxArea = max(area, maxArea)
                    _r -= 1

        return maxArea

    def maximalRectangle2(self, matrix: List[List[str]]) -> int:
        """
        Observe that each position can be the top right corner of a rect

        Idea, use prefix sum tech to sum the mat, to quickly look up area sum.

        then for each position, for each number of cols, and for each row after in that potential rect,
        check if sum is consistent, this validate the rect is valid.

        Complexity, O(n *  m) * O(n + m), roughly O(n^3)
        """

        mem = []
        for _ in range(len(matrix)):
            arr = [0] * len(matrix[0])
            mem.append(arr)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                s = int(matrix[r][c])

                if r > 0:
                    s += mem[r - 1][c]
                if c > 0:
                    s += mem[r][c - 1]
                if r > 0 and c > 0:
                    s -= mem[r - 1][c - 1]

                mem[r][c] = s
        peak = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] != "1":
                    continue
                maxCol = len(matrix[0])
                for _r in range(r, len(matrix)):
                    for _c in range(c, maxCol):
                        region = mem[_r][_c]
                        if r > 0:
                            region -= mem[r - 1][_c]
                        if c > 0:
                            region -= mem[_r][c - 1]
                        if r > 0 and c > 0:
                            region += mem[r - 1][c - 1]
                        if region == (_r - r + 1) * (_c - c + 1):
                            peak = max(peak, region)
                        else:
                            maxCol = _c  # fail found in _c, no need to go past it
                            break
        return peak


if __name__ == "__main__":
    o = Solution()
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    # print(o.maximalRectangle(matrix))  # expect 6
    # print(o.maximalRectangle([["1"]]))  # 1
    # print(o.maximalRectangle([["0"]]))  # 0

    mat2 = [
        ["0", "0", "1", "0"],
        ["0", "0", "1", "0"],
        ["0", "0", "1", "0"],
        ["0", "0", "1", "1"],
        ["0", "1", "1", "1"],
        ["0", "1", "1", "1"],
        ["1", "1", "1", "1"],
    ]

    # print(o.maximalRectangle(mat2))  # expect 9

    # print(o.maximalRectangle([["1", "0"], ["1", "0"]]))

    mat3 = [
        ["1", "0", "1", "1", "0", "1"],
        ["1", "1", "1", "1", "1", "1"],
        ["0", "1", "1", "0", "1", "1"],
        ["1", "1", "1", "0", "1", "0"],
        ["0", "1", "1", "1", "1", "1"],
        ["1", "1", "0", "1", "1", "1"],
    ]  # expect 8
    print(o.maximalRectangle(mat3))

    mat4 = [["0", "1", "1"],
            ["1", "0", "1"],
            ["0", "1", "1"],
            ["1", "1", "0"],
            ["0", "0", "0"],
            ["0", "1", "0"]
    ] # expect 3


    print(o.maximalRectangle(mat4   ))