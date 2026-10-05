from typing import Dict, List, Optional, Set

null = None


"""
Game plan

This question is identical to prev question, except overlapping area is now only counted once.

Idea, precalc areas for all sqrs, then do a first pass to remove dup areas.
doesn't really matter who losses the area.

Overlap area can be split/averaged for all squares collided.
"""


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        areas = []
        slices = []
        for _, y, l in squares:
            slices.append(y)
            slices.append(y + l)
        slices.sort()

        squares.sort(key=lambda s: s[0])

        for i in range(len(slices) - 1):
            y0 = slices[i]
            y1 = slices[i + 1]

            area = 0
            height = y1 - y0

            start = None
            end = None
            # calc area in slice
            for x, y, l in squares:
                if y >= y1 or y + l <= y0:
                    continue

                if start is None and end is None:
                    start = x
                    end = x + l
                    continue

                # 2 cases for future squares

                # 1. overlap
                if x < end:
                    # a) fully contained
                    if x + l <= end:
                        continue
                    else:
                        # b) partially contained, include existing part, set start to intersection
                        area += height * (end - start)
                        start = end
                        end = x + l
                        continue

                # 2. no overlap
                area += height * (end - start)
                start = x
                end = x + l


            if start is not None and end is not None:  # process last segment
                area += height * (end - start)

            if area:
                areas.append((y0, y1, area))
        half = sum(a[2] for a in areas) / 2
        cur = 0
        epsilon = 10**(-5)
        for y0, y1, area in areas:
            cur += area
            if abs(half - cur) < epsilon:
                return y1
            if cur > half:
                _area = cur - area
                diff = y1 - y0
                high = y1 - y0
                low = 0

                # bin search for the exact y val
                while True:
                    ymid = (high - low) / 2 + low
                    tempArea =( ymid / diff) * area + _area
                    if (half - tempArea) < 0:
                        high = ymid
                    else:
                        low = ymid

                    if (high - low) < epsilon:
                        return y0 + ymid


if __name__ == "__main__":
    o = Solution()
    # print(o.separateSquares([[0,0,1], [2, 2, 1]]))
    print(o.separateSquares([[15,21,2],[19,21,3]]))
    # print(o.separateSquares([[0, 0, 2], [1, 1, 1], [1, 1, 1]]))
