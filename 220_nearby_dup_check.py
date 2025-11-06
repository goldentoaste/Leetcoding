from typing import List, Set, Dict, Optional
null = None

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        '''
        GamePlan, use sliding window of size index diff.
        Whenever window move, check if the new element is within valueDiff of any other numbers.
        '''

        window = [] # keep this sorted

        def binaryInsert(arr, val):
            low = 0
            high = len(arr) - 1

            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] == val:
                    return mid
                elif arr[mid] < val:
                    low = mid + 1
                elif arr[mid] > val:
                    high = mid - 1
            # when target is not found, bin search returns the minimum greater element
            # which is where insertion should happen.
            return low

        def binaryRange(arr, minVal, maxVal):
            '''
            use binary search to check if there is a number in range of a sorted list
            '''

            low = 0
            high = len(arr) - 1

            while low <= high:
                mid = low + (high - low) // 2
                val = arr[mid]
                if val < minVal:
                    # mid is too low, try increasing
                    low = mid + 1
                elif val > maxVal:
                    # mid too large, try decreasing
                    high = mid - 1
                else:
                    # mid is within range
                    return True
            return False

        for i, n in enumerate(nums):
            if binaryRange(window, n - valueDiff, n + valueDiff):
                return True

            window.insert(binaryInsert(window, n),n)

            if len(window) > indexDiff:
                window.remove(nums[i - indexDiff])

        return False



if __name__ == "__main__":
    o = Solution()

    print(o.containsNearbyAlmostDuplicate(
        nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
    )) # true

    print(o.containsNearbyAlmostDuplicate(
        nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
    )) # false