from typing import List, Set, Dict, Optional

from math import ceil
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        """
        game plan, model this question using a monotonic function, then binary search on its domain

        let f(k) -> _h be the function of how many hours koko needs to eat all the nanas 
        when can now use binary search for the minimum k such that f(k) = k
        """

        def eat(arr, rate):
            out = 0
            for nana in arr:
                out += ceil(nana / rate)
            return out

        low = 1
        high = max(piles)
        while low < high:
            candidate = low + (high - low) // 2
            hours = eat(piles, candidate)
            print(candidate, hours)
            if hours == h:
                high = candidate  # can finish
            elif hours > h:  # eating too slow, need more hours to finish. So we choose to search faster speed
                low = candidate + 1
            elif hours < h:  # eating too fast, could eat slow since we finished ahead of schedule
                high = candidate
        return low


if __name__ == "__main__":
    o = Solution()
    print(o.minEatingSpeed([3,6,7,11], h = 8))
    print(o.minEatingSpeed([30, 11, 23, 4, 20], h=5))
    print(o.minEatingSpeed([30, 11, 23, 4, 20], h=6))
