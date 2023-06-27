from typing import List, Set, Dict, Optional, Self


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """


if __name__ == "__main__":
    o = Solution()


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
            root = queue.pop(0)
            left = l.pop(0)
            right = l.pop(0)
            root.left = left
            root.right = right

            queue.append(left)
            queue.append(right)

        return root

    def __str__(self):
        out = str(self.val)

        if self.left:
            out += str(self.left)
        if self.right:
            out += str(self.right)
        return out
