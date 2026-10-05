from typing import List, Set, Dict, Optional
null = None
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        O(26) is constant...

        use sliding window and keep a counter of letters in the counter.
        if windowsize - count of most freq letter < k, replacement is possible.
        '''

        mem = [0] * 26
        def mostFreq():
            index = 0
            peak = mem[0]
            for i, p in enumerate(mem):
                if p > peak:
                    peak = p
                    index = i

            return index

        longest = 0
        left = 0
        A = ord('A')
        for right, c in enumerate(s):
            mem[ord(c) - A] += 1
            peak = mem[mostFreq()]
            while (right - left + 1 - peak) > k:
                mem[ord(s[left]) - A] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest

if __name__ == "__main__":
    o = Solution()
    # print(o.characterReplacement( "ABAB", k = 2)) # 4
    # print(o.characterReplacement("AABABBA", k = 1)) # 4

    print(o.characterReplacement('DPDPFP', 2))