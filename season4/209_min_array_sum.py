

from typing import List, Set, Dict, Optional
null = None



class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        use sliding window.
        - grow window in each iteration
        - check if sum of array is >= target.
        - try shrink the window when window sum is >= target, to find the min array size.
        '''


        windowSum = 0
        left = 0

        out = float('inf')
        for right, n in enumerate(nums):
            windowSum += n

            while windowSum >= target:
                out = min(right - left + 1, out)
                windowSum -= nums[left]
                left+= 1

        if out == float('inf'):
            return 0
        return out

if __name__ == "__main__":
    o = Solution()
    print(o.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])) # 1
    print(o.minSubArrayLen(target = 4, nums = [1,4,4])) # 2
    print(o.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1])) # 0