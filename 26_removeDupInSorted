from typing import List, Set, Dict, Optional


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
        return len(nums)
    
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # fast and slow pointer
        # no need to remove items
        slow = 1
        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
        return slow

if __name__ == "__main__":
    o = Solution()
    l = [0,0,1,1,1,2,2,3,3,4]
    print(o.removeDuplicates(l)) # expect 5
    
    print(l) # expect [0 1 2 3 4]