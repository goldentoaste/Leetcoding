from typing import List, Set, Dict
from collections import defaultdict
class Solution(object):
    
    # check if s and t are anagram of each other
    def isAnagram(self, s, t):
        """
            :type s: str
            :type t: str
            :rtype: bool
        """
        
        mem1 = defaultdict(lambda: 0)
        mem2 = defaultdict(lambda: 0)
        
        for letter in s:
            mem1[letter] += 1
        
        for letter in t:
            mem2[letter] += 1
        
        return mem1 == mem2


if __name__ == '__main__':
    o = Solution()