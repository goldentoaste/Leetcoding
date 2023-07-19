




from typing import List, Set, Dict, Optional

class Solution(object):
    def missingNumber(self, nums : list):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (len(nums) * (len(nums)+1) // 2) - sum(nums)


if __name__ == "__main__":
    o = Solution()
    
    
    print(o.missingNumber([1, 3, 4, 0]))
    