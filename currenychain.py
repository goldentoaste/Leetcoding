from collections import deque
from typing import List, Set, Dict, Optional, Tuple


class Solution:
    def solveCurrency(self, conversions: List[Tuple[str, str, str]], source: str, target: str):
        # return -1 if conversion isnt possible

        twoWayMap: Dict[str : Dict[str, float]] = dict()

        # set graph relations for units
        for con in conversions:
            a, b, rate = con

            if a not in twoWayMap:
                twoWayMap[a] = {b: rate}
            else:
                twoWayMap[a][b] = rate

            if b not in twoWayMap:
                twoWayMap[b] = {a: 1 / rate}
            else:
                twoWayMap[b][a] = 1 / rate

        # traverse to the from source to targeet.
        queue = [(source, 1)]

        while queue:
            temp = []
            for name, val in queue:

                if name not in twoWayMap:
                    continue

                currencies = twoWayMap[name]
                if target in currencies:
                    return val * currencies[target]
                else:
                    for nextName, nextVal in currencies.items():
                        temp.append((nextName, val * nextVal))
                    twoWayMap.pop(name)  # remove current key to prevent revisiting old nodes
            queue = temp

        return -1


if __name__ == "__main__":
    o = Solution()

    print(
        o.solveCurrency(
            [
                ["USD", "JPY", 110],
                ["USD", "AUD", 1.45],
                ["JPY", "GBP", 0.0070],
            ],
            "GBP",
            "AUD",
        ),
    )
