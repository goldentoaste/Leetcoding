from typing import List, Set, Dict, Optional

null = None


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """
        Find length of longest subarray in which the entire range is strictly increase or decrease.
        This can naturally be solved with sliding window, since we are finding continous array with some property, which is monotonic.
        """

        if not nums:
            return 0

        maxLen = 1
        left = 0  # start of window, just to calc length
        increase = False

        for right in range(1, len(nums)):
            n = nums[right]

            if n == nums[right - 1]:
                left = right
                continue

            currentIncrease = n > nums[right - 1]

            if currentIncrease == increase:
                # doesn't matter is increase is true or false
                # matching => monotone still
                maxLen = max(right - left + 1, maxLen)
            else:
                # 2 distinct number must be either increase or decrease
                left = right - 1
                increase = n > nums[right - 1]
        return max(maxLen, len(nums) - left)


if __name__ == "__main__":
    o = Solution()
    print(o.longestMonotonicSubarray([1, 3, 4]))
