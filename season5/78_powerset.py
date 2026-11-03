from typing import List, Set, Dict, Optional

null = None


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        Given a list of numbers, return the powerset of the numbers, that is, every possible subset.

        Example:
        1, 2, 3 ->
        [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

        Logics:
        start with a empty set, then scan left to right, either include or don't include each element.
        Can either be done with recursion or stack. Recursion is more intuitive.

        Running time 2^n, since powerset is all possible subsets, each element can be either included or excluded, leading to total 2^n combinations.
        """

        out = []

        def powerSet(cur: list[int], rem: list[int]):
            out.append(list(cur))

            for i in range(len(rem)):
                e = rem[i]
                cur.append(e)

                # use [i + 1:] here since if we are trying a number, all previous number would've been tried already.
                powerSet(cur, rem[i + 1 :])
                cur.pop()

        powerSet([], nums)
        return out


if __name__ == "__main__":
    o = Solution()
    print(o.subsets([1, 2, 3]))
