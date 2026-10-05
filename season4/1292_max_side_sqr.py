from typing import Dict, List, Optional, Set

null = None


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        """
        Idea, first compute a prefix sum 2d array, so that regions' sum can be computed in constant time.

        then try diff side lengths.
        """
        mem = [([0] * len(mat[0])) for _ in range(len(mat))]

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                total = mat[r][c]

                if r > 0:
                    total += mem[r - 1][c]
                if c > 0:
                    total += mem[r][c - 1]
                if r > 0 and c > 0:
                    total -= mem[r - 1][c - 1]
                mem[r][c] = total

        def find_a_sqaure(side: int):
            if side == 0:
                return True

            for r in range(len(mat)):
                for c in range(len(mat[0])):
                    if r - side + 1 < 0 or c - side + 1 < 0:
                        continue
                    val = mem[r][c]
                    if r - side >= 0:
                        val -= mem[r - side][c]
                    if c - side >= 0:
                        val -= mem[r][c - side]
                    if  r - side >= 0 and c - side >= 0:
                        val += mem[r - side][c - side]
                    if val <= threshold:
                        return True
            return False

        low = 0
        high = min(len(mat), len(mat[0]))

        while low <= high:
            mid = ((high - low) // 2) + low
            search = find_a_sqaure(mid)
            if not search:
                high = mid - 1
            else:
                # try a higher val
                low = mid + 1
        return low - 1


if __name__ == "__main__":
    o = Solution()
    print(o.maxSideLength( mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4))
    print(
        o.maxSideLength(
            mat=[[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]], threshold=1
        )
    )
