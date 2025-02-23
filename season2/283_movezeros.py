from typing import List, Set, Dict, Optional

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        slow = 0
        for fast in nums:
            if fast:
                nums[slow] = fast
                slow += 1
                
        for i in range(slow, len(nums)):
            nums[i] = 0

if __name__ == "__main__":
    o = Solution()
    
    l = [0,1,0,3,12] 
    o.moveZeroes(l)
    print(l) # expect zeros to be at the end.