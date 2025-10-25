

from typing import List, Set, Dict, Optional
null = None

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        zerosAllowed = k
        maxSize = 0

        left = 0
        for right, n in enumerate(nums):
            if n == 0:
                zerosAllowed -= 1
            while zerosAllowed < 0 and left < right:
                if nums[left] == 0:
                    zerosAllowed += 1
                left += 1
            maxSize = max(maxSize, right - left + 1)

        return maxSize

if __name__ == "__main__":
    o = Solution()
    print(o.longestOnes([1,1,1,0,0,0,1,1,1,1,0], k = 2)) # expect 6
    print(o.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 0)) # 10