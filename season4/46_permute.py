
from typing import List, Set, Dict, Optional
null = None


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        give this list of nums, return all possible permutations
        """

        out = []

        def process(cur: List[int], remain: Set[int]):
            if not remain:
                out.append(list(cur))
            else:
                for r in list(remain):
                    cur.append(r)
                    remain.remove(r)

                    process(cur, remain)

                    remain.add(cur.pop())
        process([], set(nums))
        return out





if __name__ == "__main__":
    o = Solution()
    print(o.permute([1, 2, 3]))