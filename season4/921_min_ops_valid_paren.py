

from typing import List, Set, Dict, Optional


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        mismatch = 0

        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if not stack or stack[-1] != "(":
                    mismatch += 1
                else:
                    stack.pop()
            else:
                print("???")
        return mismatch + len(stack)

if __name__ == "__main__":
    o = Solution()
    print(o.minAddToMakeValid("((()")) # 2
    print(o.minAddToMakeValid("()))))"))