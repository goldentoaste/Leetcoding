

from typing import List, Set, Dict, Optional
null = None

class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        strats: 2 options
        Plan A;
        1. splice string into words
        2. put words in a list
        3. reverse list
        4. join revered list as a string

        Plan B:
        1. reverse entire string
        2. reverse each word

        especially in python, both approach is about the same, lets use plan B
        '''

        s = s[::-1]
        out = ""
        prev = 0
        curr = 0 # prev marks the start with a word, then iter curr until a word is found

        while True:
            if curr >= len(s): # entire string is processed
                break
            # remove as much space as possible
            while curr < len(s) and s[curr] == ' ':
                curr += 1
            prev = curr

            # can be sure prev is at a real char now
            while curr < len(s) and s[curr] != ' ':
                curr += 1

            if curr > prev:
                # at this point, curr is either at end of string, or end of word
                out += ('' if not out else ' ') + (s[prev:curr])[::-1]
                
        return out





if __name__ == "__main__":
    o = Solution()
    s = "a good   example"
    print(o.reverseWords(s)) # expect: example a good