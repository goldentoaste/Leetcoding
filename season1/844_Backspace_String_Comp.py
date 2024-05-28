class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        
        return self.processString(s) == self.processString(t)
    
    def processString(self, s):
        
        temp = ""
        
        for char in s:
            if char == "#":
                temp = temp[:-1]
            else:
                temp += char
        return temp
if __name__ == "__main__":
    
    s = Solution()
    print(s.backspaceCompare("a#b#", "xy##c"))