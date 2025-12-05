
from typing import List, Set, Dict, Optional
null = None


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mem = dict()

        def recur(a, b):
            if (a, b) in mem:
                return mem[(a, b)]

            if a == -1 and b != -1:
                return b

            if b == -1 and a != -1:
                return a

            if a == -1 and b == -1:
                return 0

            if word1[a] == word2[b]:
                return recur(a - 1, b - 1)

            minOps = min(
                recur(a, b - 1), # insert
                recur(a - 1, b), #delete
                recur(a - 1, b - 1) # replace
            ) + 1

            mem[(a, b)] = minOps

            return minOps

        test = []
        for row in range(len(word2)):
            test.append([])
            for col in range(len(word2)):
                test[row].append(mem[row, col])
            print(test[row])


        return recur(len(word1) - 1, len(word2) - 1)

if __name__ == "__main__":
    o = Solution()
    print(o.minDistance('intention', 'execution'))