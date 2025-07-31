from typing import Dict, List, Optional, Set



class Solution:
    def rob(self, nums: List[int]) -> int:
        mem : Dict[int, int] = dict()
        
        def dp(index):
            if index < 0:
                return 0
            
            if index in mem:
                return mem[index]
            
            val = max(nums[index] + dp(index - 2), dp(index - 1))
            mem[index] = val
            return val
        
        return dp(len(nums) - 1)
            
        


if __name__ == "__main__":
    o = Solution()
    print(o.rob([1,2,3,1]
))
