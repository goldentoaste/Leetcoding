
from typing import List, Set, Dict, Optional




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #  find longest substr with no dup
        mem = set()

        maxLen = 0
        low = 0
        for char in s:
            if char not in mem:
                mem.add(char)
                maxLen = max(maxLen, len(mem))
            else:
                while char in mem:
                    if s[low] in mem:
                        mem.remove(s[low])
                    low += 1
                mem.add(char)

        return max(len(mem), maxLen)


if __name__ == "__main__":
    o = Solution()
    print(o.lengthOfLongestSubstring("aab"))
    # print(o.lengthOfLongestSubstring("abcabcbb"))
    # print(o.lengthOfLongestSubstring("bbbb"))