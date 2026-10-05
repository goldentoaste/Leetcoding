

from typing import List, Set, Dict, Optional


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxzy"}

        mem = [""]

        for d in digits:
            letters = mapping[d]

            newMem = []
            for i in range(len(mem) - 1, -1, -1):
                for l in letters:
                    newMem.append(mem[i] + l)

            mem = newMem

        return mem


if __name__ == "__main__":
    o = Solution()
    print(o.letterCombinations("23"))