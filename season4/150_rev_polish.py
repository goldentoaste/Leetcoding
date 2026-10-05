

from typing import List, Set, Dict, Optional
null = None
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in ('+', '-', '/', '*'):
                stack.append(int(t))
                continue

            b = stack.pop()
            a = stack.pop()
            val = 0

            if t == '+':
                val = a + b
            elif t =='-':
                val = a - b
            elif t =='*':
                val = a * b
            elif t =='/':
                val = a / b
                val = int(abs(val)) * (-1 if val < 0 else 1)
            stack.append(val)

        return stack[0] # tokens will be given in a way to always be valid

if __name__ == "__main__":
    o = Solution()
    print(o.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))