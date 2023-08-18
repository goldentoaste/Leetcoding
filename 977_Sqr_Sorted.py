from typing import List, Set, Dict, Optional


class Solution:
    def sortedSquares(self, nums: List[int]):
        cross = 0
        for i in range(1, len(nums)):
            if nums[i] >= 0 or i == len(nums) - 1:
                cross = i
                break
    
        pos = [x * x for x in nums[cross:]]
        neg = [x * x for x in reversed(nums[:cross])]
        out = []
        p = 0
        n = 0
        while p < len(pos) and n < len(neg):
            if pos[p] < neg[n]:
                out.append(pos[p])
                p += 1
            else:
                out.append(neg[n])
                n += 1
        if p < len(pos):
            out.extend(pos[p:])
        if n < len(neg):
            out.extend(neg[n:])

        return out


if __name__ == "__main__":
    o = Solution()

    print(o.sortedSquares([-4, -1, 0, 3, 10]))  # expect [0, 1, 9, 16]
    print(o.sortedSquares([1, 2, 3, 4])) 