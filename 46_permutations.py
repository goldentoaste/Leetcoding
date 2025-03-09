from typing import List, Set, Dict, Optional

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        
        def perm(cur: List[int], rest: List[int]):
            if len(rest) == 0:
                out.append([*cur])
                return
            
            for i, n in enumerate(rest):
                cur.append(n)
                perm(cur, rest[:i] + rest[i+1:])
                cur.pop(-1)
        
        perm([], nums)
        return out

if __name__ == "__main__":
    o = Solution()
    print(o.permute([1, 2, 3]))
    print(o.permute([0, 1]))