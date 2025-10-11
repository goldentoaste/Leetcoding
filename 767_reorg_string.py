from typing import Dict, List, Optional, Set


class Solution:
    def reorganizeString(self, s: str) -> str:

        mem = [0] * 26
        for c in s:
            mem[ord(c) - ord('a')] += 1

        letters = [[chr(idx + ord('a')),  val] for idx, val in enumerate(mem) if val > 0]
        letters.sort(key=lambda x:x[1])

        out = ""
        left = True
        while len(out) < len(s):
            if left:
                out += letters[0][0]
                letters[0][1] -= 1

                if letters[0][1] == 0:
                    letters.pop(0)
            else:
                out += letters[-1][0]
                letters[-1][1] -= 1

                if letters[-1][1] == 0:
                    letters.pop()

            if len(out) >= 2:
                print(out)
                if out[-1] == out[-2]:
                    return ""

        return out



if __name__ == "__main__":
    o = Solution()
    print(o.reorganizeString("aab")) # expect aba
    print(o.reorganizeString("aaab")) # expect "" (no solution)