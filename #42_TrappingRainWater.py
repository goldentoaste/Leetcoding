####
# https://leetcode.com/problems/trapping-rain-water/
####

from typing import List
from collections import defaultdict
class Solution:
    def trap(self, height: List[int]) -> int:

        peakHeight = height[0]

        water = 0
        waterQueue = defaultdict(lambda:0)

        for cur in height:
            print(waterQueue)
            for i in range(cur):
                if waterQueue[i] > 0:
                    water += 1
                    waterQueue[i] -= 1

            if cur >= peakHeight:
                peakHeight = cur
                waterQueue.clear()
                continue
            else:
                # cur must be less
                for i in range(cur + 1):
                    waterQueue[i] += 1


        return water


if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # expect 6