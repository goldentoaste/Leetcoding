from typing import List, Set, Dict, Optional


def isBadVersion(version):
    return version == 4


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        low = 1
        high = n
        mid = (low + high) // 2

        while low < high:
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
            mid = (low + high) // 2

        return mid


if __name__ == "__main__":
    o = Solution()
    print(o.firstBadVersion(5))
