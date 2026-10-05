

from typing import List, Set, Dict, Optional
null = None




class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        still generate all possible subset, but avoid branching when an element is same as prev element.
        note the repeated should still be used at some point
        '''
        nums.sort()
        out = []
        def backtrack(mem:list, index:int):
            '''
            mem: elements included in the subset so far
            index: only consider elements of nums including and after index.
            '''
            out.append(list(mem))

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue # avoid branching when dups are encountered, but still at least use it once for each recursion depth.
                mem.append(nums[i])
                backtrack(mem, i + 1)
                mem.pop()
        backtrack([], 0)

        return out

if __name__ == "__main__":
    o = Solution()
    print(o.subsetsWithDup([1,2,2])) # [[],[1],[1,2],[1,2,2],[2],[2,2]]
    print(o.subsetsWithDup([4, 4, 4, 1, 4]))