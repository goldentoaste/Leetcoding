from typing import List, Set, Dict, Optional
import math


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<=0:
            return True
        original = x
        count = int(math.log10(x))
        total = 0
        while x > 0:
            total += x % 10 * 10**count
            x = x // 10
            count -= 1

        return total == original


if __name__ == "__main__":
    o = Solution()

    print(o.isPalindrome(-1))
