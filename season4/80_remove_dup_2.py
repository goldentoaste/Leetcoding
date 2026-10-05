from typing import Dict, List, Optional, Set


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        low = 0

        for high in range(len(nums)):
            if high == len(nums) - 2:
                print(nums, low)
                print(nums[high],nums[low], low < 2,  nums[low - 1] != nums[low - 2])
            if nums[high] != nums[low] or low < 2  or nums[low - 1] != nums[low - 2]:
                nums[low] = nums[high]
                low += 1

        return low


if __name__ == "__main__":
    o = Solution()
    arr = [0, 1, 2, 2, 2, 2, 2, 3, 4, 4, 4]
    idx = o.removeDuplicates(arr)
    print(arr[:idx])
