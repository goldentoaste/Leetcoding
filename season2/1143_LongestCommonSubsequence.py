from typing import List, Set, Dict, Optional


class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:

        mem = [[0] * (len(B) + 1) for _ in range(len(A) + 1)] # TODO optimize for only current row and prev row
        
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                
                if A[i - 1] == B[j - 1]:
                    # def a common char
                    mem[i][j] = mem[i-1][j-1] + 1
                else:
                    mem[i][j] = max(mem[i][j-1], mem[i-1][j]) # try without a common char
        return mem[len(A)][len(B)]


if __name__ == "__main__":
    o = Solution()
    print(o.longestCommonSubsequence("abcde", "ace")) # expect 3