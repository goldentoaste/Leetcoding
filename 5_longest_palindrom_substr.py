from typing import List, Set, Dict, Optional

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def palindrome(left: int, right:int, targetLength:int):
            while left > 0 and right < len(s) - 1 and (s[left - 1] == s[right + 1]):
                left -= 1
                right += 1
            return s[left: right + 1]

        maxLength = 1
        maxString = s[0]
        for center in range(len(s)):

            # center is left of even palindrome
            even = palindrome(center + 1, center, maxLength)
            if len(even) > maxLength:
                maxString = even
                maxLength = len(maxString)


            odd = palindrome(center, center, maxLength)
            if len(odd) > maxLength:
                maxString = odd
                maxLength = len(maxString)

        return maxString


if __name__ == "__main__":
    o = Solution()
    print(o.longestPalindrome("babad")) # expect bab or aba
    print(o.longestPalindrome("aaaa")) # expect aaaa
