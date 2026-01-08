from typing import Dict, List, Optional, Set

null = None


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        mem = dict()

        def recurse(i1, i2):
            if (i1, i2) in mem:
                return mem[(i1, i2)]
            if i1 < 0 or i2 < 0:
                return float("-inf")

            best = max(
                max(0, recurse(i1 - 1, i2 - 1)) + nums1[i1] * nums2[i2],  # if the current index is chosen
                recurse(i1 - 1, i2),
                recurse(i1, i2 - 1),
            )

            mem[((i1, i2))] = best
            return best
        
        return recurse(len(nums1) - 1, len(nums2) - 1)

    def maxDotProduct1(self, nums1: List[int], nums2: List[int]) -> int:
        """
        find the max dot product of 2 sub sequence from nums1 and nums2, both sub seq non empty

        Strategy, brute force with backtracking?

        Observations
        * Non-empty -> start with -inf so that any choice is valid
        * Choices made during brute force should be monotone increasing.
            + is it really monotonic though?
            + yes it is, we are not forced to make any choices
        * How to represent state?
            * Dot product vector should be at most length min(n1.length, n2.length)
            * have a limit for N1 and N2, for positions already tried.
            * have a current value
            * a global max val

        * Procedures
            + for each digit in N1, try to pair it with a digit in N2.
                + also try if the digit is not included.

            + Advance limit for N2, recurse.
            + update max if needed.
        """

        maxVal = float("-inf")
        length1 = len(nums1)
        length2 = len(nums2)

        def recurse(n1Index, n2Index, val):
            nonlocal maxVal
            if n1Index >= length1 or n2Index >= length2:
                return
            digit1 = nums1[n1Index]

            for index2, digit2 in enumerate(nums2[n2Index:]):
                prod = digit1 * digit2
                added = val + prod
                if added < val and prod < maxVal:
                    continue
                maxVal = max(maxVal, added)
                recurse(n1Index + 1, index2 + n2Index + 1, val + prod)

            # also consider if current digit in n1 is just skipped
            recurse(n1Index + 1, n2Index, val)

        recurse(0, 0, 0)
        return maxVal


if __name__ == "__main__":
    """
    worst case n^2
    """
    o = Solution()
    print(o.maxDotProduct([2, 1, -2, 5], [3, 0, -6]))  # expect 18
    print(
        o.maxDotProduct(
            [
                -5,
                -1,
                -2,
            ],
            [3, 3, 5, 5],
        )
    )  # expect -3
    print(
        o.maxDotProduct(
            [0, 4, -6, 8, 10, 3, 7, 15, -15, -1, -6, -13, 2, -6, -9, 9, -7, -6],
            [1, 12, 9, -7, 2, 9, -2, 0, -10, -12, 14, -15, -7, -9, 4, 15, -6, 2],
        )
    )
