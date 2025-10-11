
from typing import List, Set, Dict, Optional


from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        strat:
        want basically list every range that sums to k, however nums could contain negatives
        -> sum function is not monotonic, so sliding window isn't applied.

        build a prefix sum, and a map
        map each sum to the ending index. can have muliple index, each position should be list.
        '''
        mem = defaultdict(list)
        mem[0].append(-1) # empty sum
        accu = 0

        total = 0
        for i, n in enumerate(nums):
            accu += n
            diff = accu - k

            if diff in mem:
                total += len(mem[diff])

            mem[accu].append(i)

        return total



if __name__ == "__main__":
    o = Solution()
    print(o.subarraySum([1,2,3], k = 0)) # expect 2

    print(o.subarraySum([1,2,3], k = 3)) # expect 2
    print(o.subarraySum([1,1,1], k = 3)) # expect 1
    print(o.subarraySum([1,1,1], k = 2)) # expect 2

