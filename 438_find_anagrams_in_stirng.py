from typing import List, Set, Dict, Optional
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(s) < len(p):
            return []
        ref = Counter(p)
        cur = Counter(s[: len(p)])

        out = []

        plength = len(p)

        for high in range(plength, len(s) + 1):
            low = high - plength
            if ref == cur:
                out.append(low)

            if high < len(s):
                cur[s[high]] += 1

            cur[s[low]] -= 1
            if cur[s[low]] == 0:
                cur.pop(s[low])

        return out


if __name__ == "__main__":
    o = Solution()

    print(o.findAnagrams("cbaebabacd", "abc"))  # expect [0, 6]
    print(o.findAnagrams("abab", "ab"))  # expect [0, 1, 2]
