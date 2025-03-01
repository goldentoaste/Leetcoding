from collections import defaultdict
from typing import Dict, List, Optional, Set


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        def freqMap(txt: str):
            mem = defaultdict(int)  # defaults to 0 integer
            for s in txt:
                mem[s] += 1
            return mem

        cur = defaultdict(int)
        target = freqMap(t)

        validCount = 0
        targetCount = len(t)

        left, right = 0, 0
        resLeft, resRight = 0, float("inf")

        out = ""

        while right < len(s):
            c = s[right]

            cur[c] += 1

            if c in target and cur[c] <= target[c]:
                # then this char is needed in target
                validCount += 1

            right += 1

            # add chars to mem until there is a match

            # then shrink to find min window
            while validCount == targetCount:
                c = s[left]
                if c in target and target[c] == cur[c]:
                    validCount -= 1
                    if validCount < targetCount:
                        if right - left < resRight - resLeft:
                            # new best is found
                            resRight = right
                            resLeft = left
                            out = s[resLeft:resRight]
                cur[c] -= 1
                left += 1
    
        return out


if __name__ == "__main__":
    o = Solution()
    print(o.minWindow("ADOBECODEBANC", "ABC"))  # expect "BANC"

    print(o.minWindow("aa", "aa"))  # expect 'aa'
    
    print(o.minWindow("bdab", "ab")) # expect 'ab'
