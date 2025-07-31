from typing import Dict, List, Optional, Set


class Solution:
    def rob(self, nums: List[int]) -> int:
        # same as house robber except circular house
        if len(nums) == 1:
            return nums[0]
        

        mem: Dict[int, int] = dict()

        def dp(index, lowerLimit=0):
            if index in mem:
                return mem[index]

            if index < lowerLimit:
                return 0

            val = max(dp(index - 1, lowerLimit), dp(index - 2, lowerLimit) + nums[index])
            mem[index] = val
            return val

        withFirst = dp(len(nums) - 2)
        mem.clear()
        withLast = dp(len(nums) - 1, 1)
        return max(withFirst, withLast)


if __name__ == "__main__":
    o = Solution()
    print(o.rob([1, 2, 3, 1]))  # expect 4
    print(o.rob([2, 3, 2]))  # expect 3
    print(o.rob([1]))