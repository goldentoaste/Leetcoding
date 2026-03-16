from math import ceil
from turtle import color
from typing import List, Set, Dict, Optional

null = None


def maxPalette(colors, paletteSize, threshold):
    """
    :type colors: List[int]
    :type paletteSize: int
    :type threshold: int
    :rtype: int
    """

    colors = sorted ([int(c) for c in colors])

    count = 0
    low = 0
    for high, c in enumerate(colors):
        if high - low + 1 >= paletteSize:
            if c - colors[low] <= threshold:
                count += 1
                low = high + 1
            else:
                low += 1

    return count


if __name__ == "__main__":
    print(maxPalette([6, 2, 10, 2, 11, 1, 3, 2], 3, 4)) # expect 2
    print(maxPalette(colors= [1, 3, 3, 9, 9, 10, 10, 15], paletteSize= 4, threshold= 2)) # expect 1