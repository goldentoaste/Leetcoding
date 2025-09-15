class Solution(object):
    def numMagicSquaresInside(self, grid):
        def checkMagic(grid, row, col):
            mem = [False] * 10
            rowSum = -1

            # check row
            for r in range(row, row + 3):
                temp = 0
                for c in range(col, col + 3):
                    val = grid[r][c]
                    # range check, or unique number check
                    if val == 0 or val > 9 or mem[val]:
                        return False
                    mem[val] = True
                    temp += val
                    
                if rowSum == -1:
                    rowSum = temp
                elif temp != rowSum:
                    return False

            # cols
            for c in range(col, col + 3):
                temp = 0
                for r in range(row, row + 3):
                    temp += grid[r][c]
                if temp != rowSum:
                    return False

            # diagonals
            mainDiagonal = grid[row][col] +  grid[row + 1][col + 1 ] +  grid[row + 2 ][col + 2]
            if mainDiagonal != rowSum:
                return False
            crossDiagonal = grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col]
            if crossDiagonal != rowSum:
                return False

            return True

        def magicSqaure(grid):
            count = 0
            for row in range(0, len(grid) - 2):
                for col in range(0, len(grid[0]) - 2):
                    if checkMagic(grid, row, col):
                        count += 1
                
            return count

        return magicSqaure(grid)



if __name__ == "__main__":
    o = Solution()
    print(o.numMagicSquaresInside([[4,3,8,4],
                                   [9,5,1,9],
                                   [2,7,6,2]]))
