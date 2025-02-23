from typing import List, Set, Dict, Optional

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest = float("inf")
        maxProfit = 0
        
        for i, val in enumerate(prices):
            
            if val < lowest:
                lowest = val
            
            maxProfit = max(maxProfit, val - lowest)
        
        return maxProfit 

if __name__ == "__main__":
    o = Solution()
    print(o.maxProfit([7,1,5,3,6,4])) # expect 5
    print(o.maxProfit([7,6,4,3,1]))
