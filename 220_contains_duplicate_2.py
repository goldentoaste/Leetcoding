from collections import deque
from typing import List, Set, Dict, Optional

class Solution: 
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        
        def binaryInsert(arr, target):
            low = 0
            high = len(arr) - 1

            while low <= high:
                mid = low + (high - low) // 2               
                if target < arr[mid]:
                    high = mid - 1
                elif target > arr[mid]:
                    low = mid + 1
                else:
                    return mid
            return low
        
        def binaryRangeCheck(arr:List[int], lowBound:int, highBound:int):
            low = 0
            high = len(arr) - 1
            
            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] > highBound:
                    high = mid - 1
                elif arr[mid] < lowBound:
                    low = mid + 1
                else:
                    return True
            return False
        
        mem = []
        insertionQueue = deque([])
        
        for val in nums:
            # check if there is number in range
            if binaryRangeCheck(mem, val - valueDiff, val + valueDiff):
                return True

            # insert current number into sorted mem
            idx = binaryInsert(mem, val)
            mem.insert(idx, val)
            insertionQueue.append(val)
            
            # remove item if mem is larger than indexDiff
            if len(mem) > indexDiff:
                oldVal = insertionQueue.popleft()
                mem.pop(binaryInsert(mem, oldVal))
    
        return False

if __name__ == "__main__":
    o = Solution()
    # print(o.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3)) #expect False
    # print(o.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)) # expect True
    print(o.containsNearbyAlmostDuplicate([2, 0, -2, 2], 2, 1)) # expect false