from typing import List, Set, Dict, Optional

null = None


def _getMinimumBoxes(boxes: List[int], capacity: int) -> int:
    """
    https://aonecode.com/amazon-online-assessment/Get-Minimum-Boxes
    find out how many items to remove in order to satisfy the following
    max(boxes) <= min(boxes) * capacity

    Intuition
    We can either remove max to reduce left side
    or remove min to increase right side.
    We should choose whichever has better yield.

    sort boxes.

    while the condition is not met, check if difference between max and 2nd max is bigger than
    min * cap.
    """

    count = 0

    minIdx = 0
    boxes.sort()

    while boxes[-1] > boxes[minIdx] * capacity:
        if len(boxes) - minIdx <= 1:
            return -1  # the cond is not met, and we are about to remove everything
        diff = boxes[-1] - boxes[-2]
        if diff > capacity * boxes[minIdx]:
            boxes.pop()
        else:
            minIdx += 1
        print(boxes[minIdx:])
        count += 1

    return count

def getMinimumBoxes(boxes: List[int], capacity: int):
    boxes.sort()

    def binInsert(val):
        low = 0
        high = len(boxes)

        while low < high: # break condition low = high
            mid = low + (high - low) // 2
            if boxes[mid] > val:
                high = mid - 1
            else:
                low = mid + 1


        return low + 1

    removals = len(boxes)
    for i, val in enumerate(boxes):
        # if the remaining boxes started i, how many box do we need to remove?
        res = binInsert(val * capacity)
        removals = min(removals, len(boxes) - (res - i) + 1)

    return removals


if __name__ == "__main__":
    print(getMinimumBoxes(boxes=[1, 4, 3, 2], capacity=2))  # expect 1
    print(getMinimumBoxes(boxes=[3000, 1, 6, 40, 210], capacity=5))  # 4
    print(getMinimumBoxes(boxes=[2, 3, 5, 20, 25], capacity=4)) # 2