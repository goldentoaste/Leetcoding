from typing import List, Set, Dict, Optional


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        out = []

        cur = []
        curSum = 0

        def inner(start):
            nonlocal curSum
            # start indicates which to try
            if curSum == target:
                out.append(cur.copy())
                return

            for i in range(start, len(candidates)):
                cur.append(candidates[i])
                curSum += candidates[i]
                if curSum < target:
                    inner(i)
                elif curSum == target:
                    out.append(cur.copy())

                curSum -= cur.pop()

        inner(0)
        return out


if __name__ == "__main__":
    o = Solution()
    print(o.combinationSum([2, 3, 5], 8))
