
from typing import List, Set, Dict, Optional


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        out = []

        cur = []

        def inner(start):
            if len(cur) == k:
                out.append(cur[:])
                return

            for i in range(start, n + 1):
                # ignore everything after start, to not repeat
                cur.append(i)
                inner(i + 1)
                cur.pop()

        inner(1)

        return out


if __name__ == "__main__":
    o = Solution()
    print(o.combine(5, 2))
