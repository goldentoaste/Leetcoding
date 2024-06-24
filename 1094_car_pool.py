from typing import Dict, List, Optional, Set


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        loads = sorted([(item[1], item[0]) for item in trips], key=lambda item: item[0])
        drops = sorted([(item[2], item[0]) for item in trips], key=lambda item: item[0])

        loadIndex = 0
        dropIndex = 0

        currentTime = 0

        while loadIndex < len(loads):

            capacity -= loads[loadIndex][1]
            currentTime = loads[loadIndex][0]

            while dropIndex < len(drops):
                dropTime, dropNum = drops[dropIndex]
                if dropTime > currentTime:
                    break
                capacity += dropNum
                dropIndex += 1

            if capacity < 0:
                return False

            loadIndex += 1

        return True


if __name__ == "__main__":
    o = Solution()
    # trips[i] = [numPassengersi, fromi, toi]
    print(o.carPooling([[2, 1, 5], [3, 3, 7]], 4))  # False
    print(o.carPooling([[2, 1, 5], [3, 3, 7]], capacity=5))  # True
