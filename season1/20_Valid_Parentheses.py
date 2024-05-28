from typing import List, Set, Dict

class Solution(object):
    def isValid(self, s:str):
        """
        :type s: str
        :rtype: bool
        """
        
        reverse = {
            ']' : '[',
            ')' : '(',
            '}' : "{"
        }
        stack = []
        
        for l in s:
            if l in reverse:
                # a closing type coming in, but there no openings to be found
                if not stack:
                    return False
                # match found
                if reverse[l] == stack[-1]:
                    stack.pop()
                # last item in stack does not match
                else:
                    return False
                # opening char coming in
            else:
                stack.append(l)
        # if there are un consumed characters, return false.
        return not stack
        
        

if __name__ == '__main__':
    o = Solution()
    
    print(o.isValid("()[]{}"))