from typing import Dict, List, Optional, Set


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1, s2 = s2, s1

        def freqMap(txt: str):
            mem = [0] * 26
            for s in txt:
                mem[ord(s) - 97] += 1
            return mem

        cur = [0] * 26
        target = freqMap(s2)
        left = 0
        for right in range(len(s1)):
            c = s1[right]
            cidx = ord(c) - 97

            cur[cidx] += 1

            while cur[cidx] > target[cidx]:
                leftIdx = ord(s1[left]) - 97
                cur[leftIdx] -= 1
                left += 1

            if cur == target:
                return True

        return False


if __name__ == "__main__":
    o = Solution()
    print(o.checkInclusion(s1="ab", s2="eidbaooo"))  # expect true
    print(o.checkInclusion(s1="ab", s2="eidboaoo"))  # expect false
