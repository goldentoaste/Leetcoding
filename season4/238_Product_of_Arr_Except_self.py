from typing import List, Set, Dict, Optional

class Solution(object):
    def productExceptSelf(self, nums: List[int]):
        if not nums or len(nums) < 2:
            return nums
        
        leftProd = [0] * len(nums)
        rightProd = [0] * len(nums)

        leftProd[0] = nums[0]
        rightProd[-1] = nums[-1]

        for i in range(1, len(nums)):
            leftProd[i] = nums[i] * leftProd[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            rightProd[i] = nums[i] * rightProd[i + 1]

        nums[0] = rightProd[1]
        nums[-1] = leftProd[-2]
        for i in range(1, len(nums) - 1):
            nums[i] = leftProd[i - 1] * rightProd[i + 1]
        return nums

if __name__ == "__main__":
    o = Solution()

    print(o.productExceptSelf([1, 2, 3, 4])) # expect [24, 12, 8, 6]