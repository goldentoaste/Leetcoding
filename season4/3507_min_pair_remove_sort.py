
from typing import List, Set, Dict, Optional
null = None




class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        ops = 0

        while True:
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    break
            else:
                return ops # all numbers are in order, ie, did not break early.

            minSum = float('inf')
            minIndex = -1
            for i in range(len(nums) - 1):
                pairSum = nums[i] + nums[i + 1]
                if pairSum < minSum:
                    minIndex = i
                    minSum = pairSum

            ops += 1
            nums[minIndex] = minSum
            nums.pop(minIndex + 1)




if __name__ == "__main__":
    o = Solution()
    print(o.minimumPairRemoval([5, 3, 2, 1]))