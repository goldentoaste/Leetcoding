from typing import List

class Solution(object):
    def longestCommonPrefix(self, strs : List[str]):
        """
        :type strs: List[str]
        :rtype: str
        """
        return strs[0][:[all((x == s[0] for x in s)) for s in zip(*strs)].index(False)]
        
        
if __name__ == "__main__":
    o = Solution()
    #strs = ["cir","car"]
    # strs = ["flower","flow","flight"]
    strs = ["dog","racecar","car"]
    print(o.longestCommonPrefix(strs))