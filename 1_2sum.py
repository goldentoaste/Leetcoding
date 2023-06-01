from typing import List, Set, Dict



class Solution(object):
    def twoSum(self, nums : List[int], target:int):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mem = {}
        for i, num in enumerate(nums):
            
            diff = target - num
            if num in mem:
                return [i, mem[num]]
            mem[diff] = i

        return []
    
    
if __name__ == '__main__':
    
    o = Solution()
    print(o.twoSum([2, 7, 11, 15], 9))