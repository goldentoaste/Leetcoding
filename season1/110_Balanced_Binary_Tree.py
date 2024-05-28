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
            out += str(self.right)
        return out


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.height(root)[0]

    def height(self, root):
        if not root:
            return True, 0

        if not root.left and not root.right:
            return True, 1
        lstat, left = True, 0
        rstat, right = True, 0

        if root.left:
            lstat, left = self.height(root.left)
        if root.right:
            rstat, right = self.height(root.right)

        return (lstat and rstat and (abs(right - left) < 2)), 1 + max(left, right)


if __name__ == "__main__":
    o = Solution()

    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(o.isBalanced(tree))  # expects true

    tree = TreeNode(
        1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2)
    )
    
    print(o.isBalanced(tree)) # expects false
