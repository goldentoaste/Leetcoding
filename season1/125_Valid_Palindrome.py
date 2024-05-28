



from typing import List, Set, Dict
import re
class Solution(object):
    def isPalindrome(self, s:str):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub("[\W_]", "", s).lower()
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return False
        return True

if __name__ == '__main__':
    o = Solution()
    
    print(o.isPalindrome("A man, a plan, a canal: Panama")) # expects, true