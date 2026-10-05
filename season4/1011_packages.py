from typing import List, Set, Dict, Optional


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        a ship has weight capacity, greater weight capacity days means few days needed
        lower capcity means more days needed

        let w = weight candidate, f(w) = days needed to ship if capacity was w, target = days
        f is a monotonic decreasing function, binary search on this function f, minimizing weight while keeping days needed equal or lower than target
        """

        # start by defining func to calc days needed given a capacity.
        def daysNeeded(weights, capacity):
            days = 1
            currentCap = capacity
            for w in weights:
                if w > currentCap:
                    days += 1
                    currentCap = capacity  # assume capacity > max weight of a single item
                currentCap -= w
            return days

        low = max(weights)
        high = sum(weights)  # over estimate upper bound

        # search range [low, high)
        while low < high:
            mid = low + (high - low) // 2
            candDays = daysNeeded(weights, mid)

            if candDays == days:
                high = mid
            elif candDays > days:
                low = mid + 1
            elif candDays < days:
                high = mid
        return low


if __name__ == "__main__":
    o = Solution()
    # print(o.shipWithinDays([1,2,3,4,5,6,7,8,9,10], days = 5)) # 15
    # print(o.shipWithinDays( [3,2,2,4,1,4], days = 3)) # 6
    # print(o.shipWithinDays([1,2,3,1,1], days = 4)) # 3
    print(o.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
