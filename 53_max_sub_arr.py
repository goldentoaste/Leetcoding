from typing import List, Set, Dict, Optional


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lastVal = nums[0]  # max arr sum in which last element was used
        maxVal = nums[0]
        for n in nums[1:]:
            lastVal = max(n, n + lastVal)
            maxVal = max(lastVal, maxVal)

        return maxVal


if __name__ == "__main__":
    o = Solution()
    print(o.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # expect 6
    print(o.maxSubArray([5, 4, -1, 7, 8]))  # expect 23
    print(o.maxSubArray([1]))  # expect 1
    print(o.maxSubArray([1, 2]))  # expect 3
    print(o.maxSubArray([8, -19, 5, -4, 20]))  # expect 21
