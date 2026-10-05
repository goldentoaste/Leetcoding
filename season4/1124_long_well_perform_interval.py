from typing import List, Set, Dict, Optional



class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        longest = 0
        mem = dict()
        curSum = 0

        for idx,  h in enumerate(hours):
            curSum +=( 1 if h > 8 else - 1)
            if curSum not in mem:
                mem[curSum] = idx

            if curSum > 0:
                longest = idx + 1

            if curSum - 1 in mem:
                longest = max(longest, idx - mem[curSum - 1])

        return longest




if __name__ == "__main__":
    o = Solution()
    print(o.longestWPI([9,9,6,0,6,6,9])) # 3
    print(o.longestWPI([5, 5, 5, 8, 8,9,9,8]))