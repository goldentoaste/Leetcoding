from collections import defaultdict
from typing import Dict, List, Optional, Set


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        out = []

        def freqMap(txt: str):
            mem = [0] * 26
            for c in txt:
                mem[ord(c) - 97] += 1

            return mem

        cur = [0] * 26
        target = freqMap(p)

        left = 0
        for right in range(len(s)):
            c = s[right]
            idx = ord(c) - 97

            cur[idx] += 1

            while cur[idx] > target[idx]:
                leftidx = ord(s[left]) - 97
                cur[leftidx] -= 1
                left += 1
            if cur == target:
                out.append(left)

        return out


if __name__ == "__main__":
    o = Solution()
    print(o.findAnagrams(s="cbaebabacd", p="abc"))  # expect [0, 6]
    print(o.findAnagrams(s="abab", p="ab"))  # expect [0, 1, 2]
