from typing import List, Set, Dict, Optional

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0] # clearly not rotated
        
        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[high]:
                # cross over point is after mid
                low = mid + 1
            else:
                high = mid - 1

        return nums[low]

if __name__ == "__main__":
    o = Solution()
    # print(o.findMin([3, 4, 5, 1, 2]))
    # print(o.findMin([4, 5, 6, 7, 0, 1 ,2]))
    # print(o.findMin([11, 13, 15, 17]))
    # print(o.findMin([3, 1, 2]))
    print(o.findMin([4,5,6,7,0,1,2]))