
from collections import defaultdict
from typing import List, Set, Dict, Optional
null = None




class Solution:
    '''
    Can't find a monotone condition since the input can be negative...


    The key, for a continuous range query, we can use a prefix sum arr, has a hashmap
    For each prefix sum, if sum - target exist in the prefix sum map, then we found a subarray. 
    This technique is harder to generalize, but still interesting.
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        accu = 0
        out = 0
        mem = defaultdict(int) # map sum to their frequency, we build and count at the same time, so only track sum we've seen so far
        mem[0] = 1

        
        for n in nums:
            accu += n
            if accu - k in mem:
                out += mem[accu - k]

            mem[accu] += 1
        return out

if __name__ == "__main__":
    o = Solution()

    print(o.subarraySum([1, 2, 3], 3))
    print(o.subarraySum([1, 1, 1], 2))