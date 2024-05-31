from typing import List, Set, Dict, Optional


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            for coin in coins:
                target = i - coin
                if target >= 0:
                    dp[i] = min(dp[i], dp[target] + 1)

        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]


if __name__ == "__main__":
    o = Solution()
    print(o.coinChange([1, 2, 5], 11))
