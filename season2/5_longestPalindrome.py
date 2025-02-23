from typing import List, Set, Dict, Optional


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pal(low, high):
            if s[low] != s[high]:
                return -1, -1
            while True:
                if low == 0 or high == len(s) - 1 or s[low - 1] != s[high + 1]:
                    break

                low -= 1
                high += 1

            return low, high

        best = 1
        maxlow, maxhigh = 0, 0

        for center in range(len(s) - 1):

            olow, ohigh = pal(center, center)
            
            if ohigh - olow + 1 > best:
                best = ohigh - olow + 1
                maxlow = olow
                maxhigh = ohigh

            elow, ehigh = pal(center, center + 1)
  
            if ehigh - elow + 1 > best:
                best = ehigh - elow + 1
                maxlow = elow
                maxhigh = ehigh

        return s[maxlow : maxhigh + 1]


class BadSolution:
    def longestPalindrome(self, s: str) -> str:
        # special cases
        if len(s) == 2 and s[0] == s[1]:
            return s

        if len(s) == 3 and s[0] == s[2]:
            return s

        longest = 1
        maxlow, maxhigh = 0, 0
        for center in range(0, len(s) - 1):

            if s[center] == s[center + 1] and (center == 0 or s[center] != s[center - 1]):
                low = center  # even center case
                high = center + 1
            else:
                # odd center case
                low = center - 1
                high = center + 1

            while (low >= 0 and high < len(s)) and s[low] == s[high]:
                dist = high - low + 1
                if dist > longest:
                    longest = dist
                    maxlow, maxhigh = low, high

                low -= 1

                high += 1

        return s[maxlow : maxhigh + 1]


if __name__ == "__main__":
    o = Solution()
    print(o.longestPalindrome("ac"))
