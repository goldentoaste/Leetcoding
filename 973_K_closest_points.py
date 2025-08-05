from typing import List, Set, Dict, Optional

from heapq import heapify, heappop

class Solution(object):
    def kClosest(self, points, k):

        points = [((x * x + y * y), (x, y)) for x, y in points] # o(n)

        heapify(points) # o(n)

        return [heappop(points)[1] for _ in range(k)] # k lg(n)


if __name__ == "__main__":
    o = Solution()
    print(o.kClosest(([3, 3], [5, -1], [-2, 4]), 2))
