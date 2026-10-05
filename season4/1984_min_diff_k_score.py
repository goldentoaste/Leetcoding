from typing import List, Set, Dict, Optional
null = None


import heapq as h

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        '''
        thoughts, in order to minimize abs diff, we want to pick numbers close to each other.
        Can sort them to naturally group numbers together.
        As in, any number group k sized picked as part of the solution should be adjacent in sorted array, since diff are minimized.


        note that list is sorted, min is always first position in window, max is always last item in window.
        '''

        nums.sort()


        minDiff = float('inf')
        for i in range(k- 1, len(nums)):
            minDiff = min(nums[i] - nums[i - k + 1], minDiff)

        return minDiff


if __name__ == "__main__":
    o = Solution()
    print(o.minimumDifference(nums = [9,4,1,7], k = 2))