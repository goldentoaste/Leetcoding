
from typing import Dict, List, Optional, Set

null = None

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        '''
        The question is really just asking for distance between 2 points, sequentially.

        We can move horizontally or vertically, or diagonally.
        hor/ver movement is measured by manhattan distance, diag is just replaces 1 hor/ver at once
        '''
        if not points or len(points) == 1:
            return 0
        lastPoint = points[0]
        total = 0
        for p in points[1:]:
            x = abs(p[0] - lastPoint[0])
            y = abs(p[1] - lastPoint[1])
            total += (x if x > y else y)
            lastPoint = p
        return total


if __name__ == "__main__":
    o = Solution()
    print(o.minTimeToVisitAllPoints( [[1,1],[3,4],[-1,0]])) # expect 7