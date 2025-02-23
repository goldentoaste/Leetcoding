from typing import List, Set, Dict, Optional


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda item: item[0])
        prev = intervals[0]
        out = 0
        for cur in intervals[1:] :
            if cur[0] < prev[1]:
                out += 1 # if current int is contained in a prev
                if cur[1] < prev[1]:
                    prev = cur # if next interval is fully contained in cur, then remove cur
            else:
                prev = cur # cur is not contained
        return out

if __name__ == "__main__":
    o = Solution()
    print(o.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]])) # expect 2
    