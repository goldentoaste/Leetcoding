from typing import List, Set, Dict, Optional

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in nums:
            if fast != val:
                nums[slow] = fast
                slow += 1
                
        
        return slow


if __name__ == "__main__":
    o = Solution()
    
    l = [1, 3, 2, 5 , 3, 2,2, 7, 3, 2, 1] 
    print(o.removeElement(l, 2),) # expect 7
    print(l) # expect no 2s exist in the first 7 elements