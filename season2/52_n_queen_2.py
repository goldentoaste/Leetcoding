from typing import List, Set, Dict, Optional


class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        """
        get number of n queens solutions.
        """

        out = 0

        cols, diag, anti_diag = [False] * n, [False] * (n * 2 - 1), [False] * (n * 2 - 1)

        def nQueens(row):
            """
            rows,cols = n items
            diag = n * 2 - 1 items, id is j-i + 9.
            anti_diag = n*2-1 items, i + j
            """
            nonlocal out

            if row >= n:
                # solution is found.
                out += 1
                return

            for col in range(n):
                # if there is already a queen here, dont put it here.
                if cols[col] or diag[col - row + n - 1] or anti_diag[row + col]:
                    continue
                # try putting a queen at (row, col)

                cols[col] = True
                diag[col - row + n - 1] = True
                anti_diag[row + col] = True

                nQueens(row + 1)

                # undo the queen placed, try another option next loop

                cols[col] = False
                diag[col - row + n - 1] = False
                anti_diag[row + col] = False

        nQueens(0)
        return out


if __name__ == "__main__":
    o = Solution()
    print(o.totalNQueens(7))
