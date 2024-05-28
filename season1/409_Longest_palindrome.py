from typing import List, Set, Dict, Optional

class Solution(object):
    def longestPalindrome(self, s:str):
        """
        :type s: str
        :rtype: int
        """
        counts = [s.count(key) for key in set(s)]
        
        hasOdd = False
        total = 0
        for count in counts:
            if not (count & 1):
                total += count
            else:
                total += count - 1
                hasOdd = True
        if hasOdd:
            total += 1
        return total
            
if __name__ == '__main__':
    o = Solution()
    
    print(o.longestPalindrome("abccccdd")) #expect 7