from typing import List, Set, Dict, Optional
from collections import defaultdict

class Solution(object):
    
    
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        mem = defaultdict(lambda:0)
        
        for n in magazine:
            mem[n] +=1

        for n in ransomNote:
            mem[n] -=1
            if mem[n] < 0:
                return False
        return True


if __name__ == "__main__":
    o = Solution()
