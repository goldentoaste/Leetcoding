from typing import List, Set, Dict, Optional



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low, high = 0, len(nums) -1
        
        while low <= high:
            mid = (low + high) // 2
            val = nums[mid]
            
            if val < target:
                low = mid + 1
            elif val > target:
                high = mid - 1
            else:
                return mid
        
        return -1
            

if __name__ == "__main__":
    o = Solution()

