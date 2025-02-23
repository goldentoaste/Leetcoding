from typing import List, Set, Dict, Optional


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        give this list of nums, return all possible permutations
        """
        out = []
        def inner(cur: List[int], remainder: List[int]):
            if not remainder:
                out.append(tuple(cur))
                return
            for id, r in enumerate(remainder):
                cur.append(r)
                inner(cur, remainder[:id] + remainder[id + 1 :])
                cur.pop()

        inner([], nums)
        return out


if __name__ == "__main__":
    o = Solution()
    print(o.permute([1, 2, 3]))
