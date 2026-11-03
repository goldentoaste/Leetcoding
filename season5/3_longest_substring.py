
from typing import List, Set, Dict, Optional
null = None


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        low = 0
        mem = set()
        maxLength = 0
        # abcabcbb
        # mem = a, low = 0
        # mem = ab, low = 0
        # mem = abc, low = 0
        # mem = bc, low = 1
        #
        for  high, c in enumerate(s):
            if c not in mem:
                mem.add(c)
                maxLength = max(maxLength, len(mem))
            else:
                print("---")
                while c in mem:
                    print(mem, s[low], c, s[:high + 1])
                    mem.remove(s[low])
                    low += 1
                mem.add(c)
        

        return maxLength

if __name__ == "__main__":
    o = Solution()
    print(o.lengthOfLongestSubstring('abcabcbb'))