from typing import List, Set, Dict, Optional


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        return power set of nums
        """

        out = [[]]
        for n in nums:
            temp = [(o + [n]) for o in out]
            out.extend(temp)
        return out


if __name__ == "__main__":
    o = Solution()
    print(o.subsets([1, 2, 3]))
