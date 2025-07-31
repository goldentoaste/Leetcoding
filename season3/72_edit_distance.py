from typing import Dict, List, Optional, Set


class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        """
        transform word1 to word2, via insert, delete, and replace operations
        return min number of steps needed to transform
        """

        mem = [[0 for _ in range(len(word2) + 1)] for __ in range(len(word1) + 1)]

        for w1 in range(1, len(word1) + 1):
            mem[w1][0] = w1
        for w2 in range(1, len(word2) + 1):
            mem[0][w2] = w2

        for w1 in range(1, len(word1) + 1):
            for w2 in range(1, len(word2) + 1):
                # delete: w1 + 1
                # insert w2 + 1
                # replace w1 + 1, w2 + 1

                if word1[w1 - 1] == word2[w2 - 1]:
                    mem[w1][w2] = mem[w1 -1][w2-1]
                else:
                    mem[w1][w2] = min(mem[w1 - 1][w2], mem[w1][w2 - 1], mem[w1 - 1][w2 - 1]) + 1

        return mem[-1][-1]


if __name__ == "__main__":
    o = Solution()
    print(o.minDistance("horse", "ros"))
