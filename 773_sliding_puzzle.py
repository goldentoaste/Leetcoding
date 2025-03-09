

from typing import List, Set, Dict, Optional, Tuple

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        def solved(b:Tuple[Tuple[int, int ,int], Tuple[int, int, int]]):
            return b == ((1, 2, 3), (4, 5, 0))

        def swap(b: tuple, x0, y0, x1, y1):
            print(b, x0, y0, x1, y1)
            if not (
                0 <= x0 < 3 and
                0 <= x1 < 3 and
                0 <= y0 < 2 and
                0 <= y1 < 2
            ):
                return None
            
            out = [[0,0,0],[0,0,0]]
            for y in range(len(b)):
                for x in range(len(b[0])):
                    if y == y0 and x == x0:
                        out[y][ x] = b[y1][x1]
                    elif y == y1 and x == x1:
                        out[y][x] = b[y0][x0]
                    else:
                        out[y][x] = b[y][x]
            return (tuple(out[0]), tuple(out[1]))
        
        mem = set()
        queue = [(tuple(board[0]), tuple(board[1]))]
        moves = 0
        while len(queue) > 0:
            items = list(queue)
            queue.clear() # transfers items to list
            
            
            for cboard in items:
                if cboard in mem:
                    continue
                
                mem.add(cboard)
                
                if solved(cboard):
                    return moves

                for y in range(2):
                    for x in range(3):
                        # can only swap with 0
                        if(cboard[y][x] == 0):
                            # swap with neighbors
                            a = swap(cboard, x, y, x + 1, y)
                            b = swap(cboard, x, y, x -1 , y)
                            c = swap(cboard, x, y, x , y + 1)
                            d = swap(cboard, x, y, x , y - 1)
                            
                            for i in (a, b, c, d):
                                if i:
                                    queue.append(i)
                                    
            moves += 1

        return -1 


if __name__ == "__main__":
    o = Solution()
    print(o.slidingPuzzle([[4,1,2],[5,0,3]])) # expect 5
