


from typing import List, Set, Dict, Optional
from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        out =deque([])

        def matchWord(text : str, startIdx : int):
            curIdx = startIdx
            while curIdx < len(s) and  text[curIdx] != " ":
                curIdx += 1

            return text[startIdx:curIdx], curIdx

        idx = 0
        while idx < len(s):
            if s[idx] == " ":
                idx += 1
            else:
                word, newIdx = matchWord(s, idx)
                out.appendleft(word)
                idx = newIdx
                print(idx)

        return " ".join(out)

    def reverseWords2(self, s: str) -> str:

        # first reverse entire string
        low = 0
        high = len(s) - 1

        while low < high:
            temp = s[high]
            s[high] = s[low]
            

if __name__ == "__main__":
    o = Solution()
    print(o.reverseWords("a good   example")) # expect: example good a