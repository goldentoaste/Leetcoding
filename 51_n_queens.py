from typing import List, Set, Dict, Optional


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        given N, the size of chess board. return all solutions to the N queens problem.
        """

        mem = [[False for _ in range(n)] for __ in range(n)]

        out = list()
        queens = 0

        def toOutput(bools: List[List[bool]]):
            return tuple(("".join([("Q" if col else ".") for col in row]) for row in bools))

        rows, cols, diag, anti_diag = [False] * n, [False] * n, [False] * (n * 2 - 1), [False] * (n * 2 - 1)

        def nQueens(row):
            """
            rows,cols = n items
            diag = n * 2 - 1 items, id is j-i + 9.
            anti_diag = n*2-1 items, i + j
            """
            nonlocal queens

            if row >= n:
                # solution is found.
                return out.append(toOutput(mem))

            for col in range(n):
                # if there is already a queen here, dont put it here.
                if rows[row] or cols[col] or diag[col - row + n - 1] or anti_diag[row + col]:
                    continue
                # try putting a queen at (row, col)
                mem[row][col] = True
                rows[row] = True
                cols[col] = True
                diag[col - row + n - 1] = True
                anti_diag[row + col] = True

                nQueens(row + 1)

                # undo the queen placed, try another option next loop
                mem[row][col] = False
                rows[row] = False
                cols[col] = False
                diag[col - row + n - 1] = False
                anti_diag[row + col] = False

        nQueens(0)
        return out


if __name__ == "__main__":
    o = Solution()
    print(o.solveNQueens(7))
