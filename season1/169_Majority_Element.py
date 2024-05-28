
from typing import List, Set, Dict, Optional

class Solution(object):
    def majorityElement(self, nums:list):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solve this in linear time and constant space
        uniques = set(nums)
        
        for i in uniques:
            if nums.count(i) > len(nums)//2:
                return i
        


if __name__ == "__main__":
    o = Solution()
