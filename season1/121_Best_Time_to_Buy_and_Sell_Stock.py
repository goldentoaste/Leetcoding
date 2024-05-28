from typing import List, Set, Dict

class Solution(object):
    def maxProfit(self, prices : List[int]):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        buyPrice = prices[0]
        best = float("-inf")
        
        for _, num in enumerate(prices, 1):
            
            if num < buyPrice:
                buyPrice = num
            else:
                if num - buyPrice > best:
                    best = num - buyPrice
        return best
        

if __name__ == '__main__':
    o = Solution()
    print(o.maxProfit([7, 1, 5, 3, 6, 4])) #expects 5