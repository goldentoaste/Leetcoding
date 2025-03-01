
from typing import List, Set, Dict, Optional


# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0 
        left = 0
        for right in range(len(height)):
            leftEle, rightEle = height[left], height[right]
            if rightEle >= leftEle:
                # start colllectin'!
                iniHeight = height[left]
                for i in range(left + 1, right):
                    water += iniHeight - height[i]
                left = right   

        if left != len(height) - 1:
            return water + self.trap(list(reversed(height[left:])))
        
        return water

if __name__ == "__main__":
    o = Solution()
    print(o.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # expect 6
