from typing import Dict, List, Optional, Set


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return nums

        low = 1

        for i in range(1, len(nums) - 1):
            if nums[i] != nums[i - 1] or nums[i] != nums[i + 1]:
                nums[low] = nums[i]
                print(i)
                low += 1

        if nums[-1] != nums[low - 1] or nums[-1] != nums[low - 2]:
            nums[low] = nums[-1]
            low += 1

        for i in range(low, len(nums)):
            nums[i] = "_"

        return nums


if __name__ == "__main__":
    o = Solution()
    print(o.removeDuplicates([1, 4, 4, 4, 4]))
