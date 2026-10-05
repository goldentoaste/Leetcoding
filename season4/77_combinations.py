from typing import List, Set, Dict, Optional
null = None



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        notice picking combinations is the same as taking the powerset, but only keep the sets with length k
        '''
        out = []
        def backtrack(mem: list):
            if len(mem) == k:
                out.append(list(mem))
                return
            start = 0 if not mem else mem[-1]
            for x in range(start + 1, n + 1): # only try numbers not seen yet.
                mem.append(x)
                backtrack(mem)
                mem.pop()
        backtrack([])
        return out
if __name__ == "__main__":
    o = Solution()
    print(o.combine(4, 2)) # expect [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]