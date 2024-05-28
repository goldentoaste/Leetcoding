from typing import List, Set, Dict, Optional


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # use 2d dp array to attack from btoh ends, [(i,j)] is the [i, ... j] substring (j included)
        
        length = len(s)
        dp = [[0] * length for _ in range(length)]
        
        for i in range(length):
            dp[i][i] = 1 # base case, if i==j, then its def a palindrome of length 1
        
        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length):
                a = s[i]
                b = s[j]
                
                if a == b:
                    if j - i == 1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j-1] , )
        return dp[0][-1]
        
        


if __name__ == "__main__":
    o = Solution()
    print(o.longestPalindromeSubseq('bbbab')) #expect 4