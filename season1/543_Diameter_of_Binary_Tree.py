from typing import List, Set, Dict, Optional, Self


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right

    @classmethod
    def fromList(cls, l: List[int]):
        root = cls(l.pop(0))
        queue = [root]

        while queue:
            item = queue.pop(0)

            if l:
                left = cls(l.pop(0))
                item.left = left
                queue.append(left)
            else:
                left = None

            if l:
                right = cls(l.pop(0))
                item.right = right
                queue.append(right)
            else:
                right = None

        return root

    def __str__(self):
        out = str(self.val)

        if self.left:
            out += str(self.left)
        if self.right:
            out += str(self.right)
        return out


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
       
        _, maxChain = self.help(root)
        return max(0, maxChain - 1)

    def help(self, root : TreeNode):
        if root.val is None:
            return 0, 0
        if not root.left and not root.right:
            return 1, 0

        left = 0
        right = 0
        leftChain = 0
        rightChain = 0
        if root.left:
            left, leftChain = self.help(root.left)

        if root.right:
            right, rightChain = self.help(root.right) 
            
        chain = max(left + right+ 1, leftChain, rightChain) 
      
        return max(left, right) + 1, chain


if __name__ == "__main__":
    o = Solution()

    nodes = TreeNode.fromList([1, 2, 3, 4, 5])

    print(o.diameterOfBinaryTree(nodes))
