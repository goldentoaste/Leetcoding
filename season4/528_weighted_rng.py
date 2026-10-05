
from typing import List, Set, Dict, Optional
null = None

from random import random
import math
class Solution:
    '''
    game plan, solve this problem in log n time.

    make a precomputed prefix sum with one extra index, such that first position is 0
    When picking a number, multiply math.random() with total, so get a number in range

    binary search for the greatest value less than target. return that index.
    '''

    def __init__(self, w: List[int]):
        self.mem = [0] * (len(w) + 1)
        for i in range(1, len(w) + 1):
            self.mem[i] += w[i - 1] + self.mem[i - 1]
        self.mem[0] = -1

    def pickIndex(self) -> int:
        target = math.floor(random() * self.mem[-1])

        low = 0
        high = len(self.mem)
        # this searches the insertion position of target, which will be the minimal upperbound within mem.
        # [low, high]
        while low < high:
            mid = low + (high - low) // 2
            val = self.mem[mid]
            if val == target:
                return mid
            elif val > target:
                high = mid
            elif val < target:
                low = mid + 1
        return low - 1

if __name__ == "__main__":
    o = Solution([10, 20, 70])
    from collections import defaultdict
    mem = defaultdict(int)

    for i in range(10000):
        idx = o.pickIndex()
        if idx == 0:
            break
        mem[idx] += 1

    for key in mem:
        print(f"{key}: {math.floor((mem[key] / 10000) * 1000) / 10}")

