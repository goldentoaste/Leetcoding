
from typing import List, Set, Dict, Optional


class NumArray:

    def __init__(self, nums: List[int]):
        
        self.sumCache = [0] * len(nums)
        
        curSum = 0
        for i in range(nums):
            curSum += nums[i]
            self.sumCache[i] = curSum
            

    def sumRange(self, left: int, right: int) -> int:
        if right < left:
            return 0
        if left == 0:
            return self.sumCache[right]
        return self.sumCache[right] - self.sumCache[left - 1]
if __name__ == "__main__":
    o = NumArray()

