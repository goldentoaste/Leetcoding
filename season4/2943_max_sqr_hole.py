
from typing import List, Set, Dict, Optional
null = None




class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        '''
        Idea, since every hbar intersects vbar,
        when a hbar is removed, if a vbar is also removed, a larger square is created.

        however, in order to make a even larger square, removing consecutive bars is needed.
        So lets find the largest amount of consecutive bars from both directions.
        '''


        hBars.sort()
        vBars.sort()

        def findLongestRun(arr:list):
            if not arr:
                return 0

            run = 1
            soFar = 1

            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    soFar += 1
                    run = max(soFar, run)
                else:
                    soFar = 1

            return run

        maxHRun = findLongestRun(hBars)
        maxVRun = findLongestRun(vBars)

        consecRuns = min(maxHRun, maxVRun) + 1

        return consecRuns * consecRuns




if __name__ == "__main__":
    o = Solution()
    print(o.maximizeSquareHoleArea( n = 2, m = 1, hBars = [2,3], vBars = [2])) # expect 4
    print(o.maximizeSquareHoleArea(n = 1, m = 1, hBars = [2], vBars = [2])) # expect 4
    print(o.maximizeSquareHoleArea(n = 2, m = 3, hBars = [2,3], vBars = [2,4])) # also expects 4