from typing import Dict, List, Optional, Set


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        mem = [0, nums[0]]
        for i, n in enumerate(nums[1:]):
            mem.append(mem[-1] + n)
        total = mem[-1]
        for i in range(1, len(nums) + 1):
            if mem[i - 1] == total - mem[i]:
                return i - 1
        return -1


if __name__ == "__main__":
    o = Solution()
    print(o.pivotIndex([1, 7, 3, 6, 5, 6]))
