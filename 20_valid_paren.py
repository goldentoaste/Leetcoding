from typing import List, Set, Dict, Optional


class Solution:
    def isValid(self, s: str) -> bool:
        parenMap = {")": "(", "}": "{", "]": "["}
        opener = set(parenMap.values())
        stack = []

        for c in s:
            if c in opener:
                stack.append(c)
                continue
            if c in parenMap:
                if not stack or stack[-1] != parenMap[c]:
                    return False
                else:
                    stack.pop()
                    continue
            return False
        return len(stack) == 0


if __name__ == "__main__":
    o = Solution()
    print(o.isValid(s="()[]{}"))  # true
    print(o.isValid(s="()]{}"))  # true
