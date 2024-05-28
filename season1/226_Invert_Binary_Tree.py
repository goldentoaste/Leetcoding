from typing import List, Set, Dict


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


class Solution(object):
    def invertTree(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.invert(root)
        return root
    
    
    def invert(self, root : TreeNode):
        if not root:return
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invert(root.left)
        self.invert(root.right)
        


if __name__ == "__main__":
    o = Solution()
    tree = TreeNode(
        4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))
    )
    print(tree)
    print(o.invertTree(tree))