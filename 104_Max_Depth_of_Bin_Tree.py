from typing import List, Set, Dict, Optional

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
    def maxDepth(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth((root.right))) + 1
        

if __name__ == "__main__":
    o = Solution()

    node = TreeNode.fromList([3,9,20,None,None,15,7])
    
    print(o.maxDepth((node)))