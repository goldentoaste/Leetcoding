from typing import Dict, List, Optional, Set

null = None


def validateSudoku(board: List[List[str]]):
    # rows
    for row in board:
        if len(row) != len(set(row)):
            return False

    for c in range(len(board)):
        col = set()
        for row in board:
            if row[c] in col:
                return False
            col.add(row[c])

    for r in range(0, 8, 3):
        for c in range(0, 8, 3):
            box = set()
            for dr in range(3):
                for dc in range(3):
                    val = board[dr + r][dc + c]
                    if val in box:
                        return False
                    box.add(val)

    return True


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Fill in the blanks sequentially, so its not possible to reach a previous state by making new choices -> no need to memo

        """

        rowCount = len(board)
        colCount = len(board[0])
        cells = rowCount * colCount

        def solver(current: List[List[str]], rows: List[Set[str]], cols: List[Set[str]], boxes: List[Set[str]], idx:int):
            '''
            returns undefined if no solution

            treat all vals before idx as solved.
            '''

            if idx == cells:
                # solved since all cells are filled
                return current

            r = idx // colCount
            c = idx % colCount

            if current[r][c] != ".":
                # this cell is already given, no need to try options for this cell
                return  solver(current, rows, cols, boxes, idx + 1)

            for opt in "123456789":
                # check if this option is valid for this cell
                if opt in rows[r] or opt in cols[c] or opt in boxes[r // 3 * 3 + c // 3]:
                    continue

                # commit the try
                rows[r].add(opt)
                cols[c].add(opt)
                boxes[r // 3 * 3 + c // 3].add(opt)
                current[r][c] = opt
                res = solver(current, rows, cols, boxes, idx + 1)

                if res:
                    # solution found
                    return res
                else:
                    # no solution, undo
                    rows[r].remove(opt)
                    cols[c].remove(opt)
                    boxes[r // 3 * 3 + c // 3].remove(opt)
                    current[r][c] = "."

            # no solution found this branch
            return None

        _rows = []
        for row in board:
            _rows.append(set(row))

        _cols = []
        for c in range(len(board)):
            _temp = set()
            for r in range(len(board)):
                _temp.add(board[r][c])
            _cols.append(_temp)


        _boxes = []
        for r in range(0, 8, 3):
            for c in range(0, 8, 3):
                box = set()
                for dr in range(3):
                    for dc in range(3):
                        val = board[dr + r][dc + c]
                        box.add(val)

                _boxes.append(box)

        return solver(board, _rows, _cols, _boxes, 0)


def matrixPrint(mat: List[List[int]]):
    for row in mat:
        print(" ".join([(str(c) if str(c) != "" else "_") for c in row]))





if __name__ == "__main__":
    o = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    solved = o.solveSudoku(board)
    matrixPrint(solved)
    print("valid?", validateSudoku(solved)
)