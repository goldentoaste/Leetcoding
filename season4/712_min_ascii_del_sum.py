from typing import Dict, List, Optional, Set

null = None


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        Observation:
        + can be broken into sub problems by taking consecutive segments starting from beginning
        + relation to prev solutions:
            f('delete', 'leet')
            - last char equal -> = f('delet', 'leet')
            - last char != -> min(f('delete', 'lee') + char('t'), f('delet', 'leet') + char('e'))
        + note state is captured by the 2 input strings, memo on these 2
        """
        mem = dict()  # map known string inputs to results, both string deletes linearly from the back, O(n^2) space

        def findMin(_s1, _s2):
            inputs = (_s1, _s2)
            if (
                inputs in mem
            ):  # seen this input before, since later we are taking all possibility, its possible arrive at a input already known.
                return mem[inputs]

            if not _s1:
                return sum(ord(c) for c in _s2)  # must del every char of s2
            if not _s2:
                return sum(ord(c) for c in _s1)  # must del every char of s1, since s2 is empty
            # note python sum() returns

            if _s1[-1] == _s2[-1]:
                # chars match, no work
                return findMin(_s1[:-1], _s2[:-1])

            # try deleting either char, return the min
            res = min(
                findMin(_s1[:-1], _s2) + ord(_s1[-1]),
                findMin(_s1, _s2[:-1]) + ord(_s2[-1])
            )
            mem[inputs] = res
            return res

        return findMin(s1, s2)


    def minimumDeleteSum2(self, s1, s2):
        '''
        alternatively, think to iterate from start of string, then decide if either char can be included.
        Use the relation defined earlier.
        Note that only state i - 1, j, and i, j - 1, and i, j are needed.

        For simplicity, have 2 linear arrays. One for current row, one for prev row.

        Let i be s1, j be s2
        '''

        # init to inf to always drop initial value
        prev = [0 for _ in range(len(s2) + 1)]
        for index, c in enumerate(s2):
            prev[index + 1] = prev[index] + ord(c)
        current = [0 for _ in range(len(s2) + 1)]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                current[0] = ord(s1[i - 1]) + prev[0]
                if s1[i - 1] == s2[j - 1]:
                    current[j] = prev[j - 1]
                else:
                    current[j] = min(
                        prev[j] + ord(s1[i - 1]),
                        current[j - 1] + ord(s2[j - 1])
                    )
            prev, current = current, prev

        return prev[-1]



if __name__ == "__main__":
    o = Solution()
    print(o.minimumDeleteSum2("sea", "eat"))  # expect 231
    print(o.minimumDeleteSum2("delete", "leet"))  # expect 403
