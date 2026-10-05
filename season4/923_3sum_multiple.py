


from typing import List, Set, Dict, Optional
from collections import defaultdict
from math import comb

class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """

        mem = defaultdict(int)

        for num in arr:
            mem[num] += 1

        items = list(mem.keys())

        sol = []
        for i in range(len(r )):
            a = items[i]

            for j in range(i, len(items)):
                b = items[j]

                for k in range(j, len(items)):
                    c = items[k]

                    if a + b + c == target:
                        t = []
                        if a == b  and b != c and  a != c:
                            t = [(comb(mem[a], 2)), mem[c]]

                        if a == c and c != b and a != b:
                            t = [comb(mem[])]
        out = 0
        print(sol)
        for a, b, c in sol:
            temp = (a * b) % (10^9 + 7)
            temp = (temp * c) % (10^9 + 7)
            out += temp

        return out



if __name__ == "__main__":
    o = Solution()
    print(o.threeSumMulti([1,1,2,2,2,2], 5))