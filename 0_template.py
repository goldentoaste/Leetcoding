from typing import List, Set, Dict, Optional



if __name__ == '__main__':
    o = Solution()
    
    
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right

    def __str__(self):
        out = str(self.val)
        
        if self.left:
            out += str(self.left)
        if self.right:
            out+= str(self.right)
        return out
    
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val : int = val
        self.next : Optional[ListNode] = next
        
    def str(self):
        return f"{self.val}" + (f", {self.next.str()}" if self.next else "]") 
    def __str__(self):
        return "[" + self.str()