
from typing import List, Set, Dict, Optional




class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]

        for n in nums:
            counts[n] +=1

        last = 0
        for idx, count in enumerate(counts):
            for i in range(count):
                nums[last] = idx
                last += 1

        return nums

if __name__ == "__main__":
    o = Solution()
    nums = [2,0,2,1,1,0]
    print(o.sortColors(nums))