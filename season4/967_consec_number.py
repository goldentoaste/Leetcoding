from typing import List, Set, Dict, Optional
null = None


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        out = []

        def back(num, rem):
            if rem == 0:
                out.append(num)
                return

            digit = num % 10

            if digit + k < 10:
                back(num * 10 + (digit + k), rem - 1)

            if digit >= k and k != 0:
                back(num * 10 + (digit - k), rem - 1)

        for i in range(1, 10):
            back(i, n - 1)

        return out

if __name__ == "__main__":
    o = Solution()
    print(o.numsSameConsecDiff( 2, 0)) # [181,292,707,818,929]