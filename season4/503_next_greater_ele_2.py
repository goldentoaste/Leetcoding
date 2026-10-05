from typing import List, Set, Dict, Optional


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # circular, so copy the input but only output this first half
        _nums = []
        _nums.extend(nums)
        _nums.extend(nums)

        stack = []
        out = []
        for n in reversed(_nums):
            # remove all elements in stack that's smaller than this item
            while stack and stack[-1] <= n:
                stack.pop()
            if not stack:
                out.append(-1)  # nothing in stack means no previous greater element
            else:
                out.append(stack[-1])
            stack.append(n)
        out.reverse()
        return out[:len(nums)]


if __name__ == "__main__":
    o = Solution()
    print(o.nextGreaterElements([1, 2, 3, 4, 3]))  # expect: [2,3,4,-1,4]
