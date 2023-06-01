from typing import List, Set, Dict

class Solution(object):
    def search(self, nums : List[int], target:int):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        
        low =0
        high = len(nums) - 1
        
        
        while low <= high:
            
            mid = (low + high) // 2
            
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                return mid
        return -1
        

if __name__ == '__main__':
    o = Solution()  
    
    print(o.search([-1,0,3,5,9,12], 9)) # expect 4