from typing import List, Set, Dict, Optional
null = None


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        '''
        game plan:

        turns out this problem is very similar if not identical to the shipping container problem, but phrased in a diff way.
        Instead of containers, we have array subdivision. Instead of days, have number of divisions.
        An observation to make is that, container problem looks for the minimum weight...which needs to be at least equal to maximum amongst sums of each container...which is what this problem is asking.

        So again, in this binary search scenario, a search param is minimized largest sum, call it S
        monotonic function is subdivision required if the max allowed sum is S, call this output D. f(S) -> D
        search target is k.

        This problem simplifies to, find the small S' such that f(S') = k
        '''

        def subarrays(arr: list, maxAllowedSum: int) -> int:
            '''
            If max allowed sum is given, whats the least amount of subdivision?
            '''

            count = 1

            currentAllocation = maxAllowedSum
            for n in arr:
                if n > currentAllocation:
                    count += 1
                    currentAllocation = maxAllowedSum
                currentAllocation -= n
            return count

        # subarray sum must be at least the max array number, no solution otherwise
        low = max(nums)
        # max subarray is just 1 division, sum the entire arr
        high = sum(nums)

        # search range [low, high). End condition: low == high
        while low < high:
            allowedSum = low + (high - low) // 2
            subArrsNeeded = subarrays(nums, allowedSum)
            if subArrsNeeded == k:
                # target reached, now look to minimize allowedSum
                high = allowedSum
            elif subArrsNeeded > k:
                # too many array needed... need to allow more sum to reduce # of arrs
                low = allowedSum + 1
            elif subArrsNeeded < k:
                # too few arrays... need to allow less to use more sub arrays
                high = allowedSum

        return low



if __name__ == "__main__":
    o = Solution()
    print(o.splitArray([7, 2, 5, 10, 8], 2))
    print(o.splitArray([1, 2, 3, 4, 5], 2))

