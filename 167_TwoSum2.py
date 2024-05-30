from typing import List, Set, Dict, Optional


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        low, high = 0, len(numbers) - 1

        while low < high:
            val = numbers[low] + numbers[high]
            if val == target:
                return (low + 1, high + 1)

            if val < target:
                # go bigger
                low += 1
            else:
                # go lower
                high -= 1

        return (-1, -1)


if __name__ == "__main__":
    o = Solution()

    print(o.twoSum([2, 7, 11, 15], 9))
