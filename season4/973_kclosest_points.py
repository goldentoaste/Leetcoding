

from typing import List, Set, Dict, Optional
import heapq as hq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[p[0] * p[0] + p[1] * p[1], p[0], p[1]] for p in points] 
        hq.heapify(points)

        out = []
        for _ in range(k):
            p = hq.heappop(points)
            out.append(p[1:])
        return out

if __name__ == "__main__":
    o = Solution()
    print(o.kClosest([[3,3],[5,-1],[-2,4]], 2)) # [[3,3],[-2,4]]