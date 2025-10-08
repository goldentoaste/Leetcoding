from typing import Dict, List, Optional, Set


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # treat 0 like -1, then we are finding the max range that sums to 0.
        #  range sum > 0 means too many 1s, sum < 0 means to many 0s.

        mem = [-1 if nums[0] == 0 else 1]

        for idx, n in enumerate(nums[1:]):
            mem.append(mem[-1] + (-1 if n == 0 else 1))

        indexMap = dict()
        maxDist = 0
        for idx, n in enumerate(mem):
            if n == 0:
                maxDist = idx + 1

            if n in indexMap:
                prev = indexMap[n]
                maxDist = max(idx - prev, maxDist)
            else:
                indexMap[n] = idx

        return maxDist


if __name__ == "__main__":
    o = Solution()
    print(o.findMaxLength([0,1,1,1,1,1,0,0,0])) # expect 6
    print(o.findMaxLength([0,1,1])) # expect 2