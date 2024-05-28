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
    def isSymmetric(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: bool
        """

        tree = []
        self.fillTree(root, tree)
        total = 0
        index = 0
        

        while total < len(tree):
            x = tree[total : total + 2**index]
            if x != list(reversed(x)):
                return False
            total += 2**index
            index += 1
        return True

    def fillTree(self, node: TreeNode, res: list):
        
        res.append(node.val)
        self.fillTreeHelper(node, res)
    
    
    def fillTreeHelper(self, node: TreeNode, res:list):
        
        if not node or node.val is None:
            return
        if node.left or node.right:
            res.append(node.left.val if node.left else None)
            res.append(node.right.val if node.right else None)
        
        self.fillTreeHelper(node.left, res)
        self.fillTreeHelper(node.right, res)
        

if __name__ == "__main__":
    o = Solution()

    t = TreeNode.fromList([1, 2, 2, None, 3, None, 3])

    print(o.isSymmetric(t))
