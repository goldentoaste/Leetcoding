from typing import List, Set, Dict, Optional


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:     
        points.sort(key=lambda item: item[0])
        prev = points[0]
        arrows = 1 # at least 1 arrow is needed for the initial balloon
        for cur in points[1:]:
            if cur[0] > prev[1]: # current baloon doesnt intersect at all
                arrows += 1
                prev = cur
            if cur[1] < prev[1]: # restrict ending for current arrow
                prev = cur
        return arrows


if __name__ == "__main__":
    o = Solution()
    print(o.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]])) #expect 2