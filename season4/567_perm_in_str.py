from typing import Dict, List, Optional, Set


class CharMap:
    def __init__(self):
        self.mem = [0] * 26
        self.ref = ord("a")

    def clear(self):
        for i in range(len(self.mem)):
            self.mem[i] = 0

    def addChar(self, char: str):
        self.mem[ord(char) - self.ref] += 1

    def removeChar(self, char: str):
        self.mem[ord(char) - self.ref] -= 1

    def contains(self, other: "CharMap"):
        for idx, c in enumerate(other.mem):
            if self.mem[idx] < c:
                return False
        return True

    def __eq__(self, other: "CharMap"):
        return other.mem == self.mem

    def hasChar(self, c: str):
        return self.mem[ord(c) - self.ref] > 0


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        check if any permutation of s1 is a substring of s2
        """

        s1Map = CharMap()
        for s in s1:
            s1Map.addChar(s)

        s2Map = CharMap()

        low = 0
        for i , s in enumerate(s2):
            if not s1Map.hasChar(s):
                s2Map.clear()
                low = i + 1
                continue
            s2Map.addChar(s)

            if i - low >= len(s1):
                s2Map.removeChar(s2[low])
                low += 1
            if s2Map ==  s1Map:
                return True

        return False


if __name__ == "__main__":
    o = Solution()
    print(o.checkInclusion(s1="ab", s2="eidbaooo"))
    # print(o.checkInclusion(s1="ab", s2="eidboaoo"))
    # print(o.checkInclusion("adc", "dcda"))