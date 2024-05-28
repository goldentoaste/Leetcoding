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


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p: TreeNode, q: TreeNode):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        pTree = [p.val]
        qTree = [q.val]

        self.fillTree(p, pTree)
        self.fillTree(q, qTree)
        print(pTree, qTree)
        return pTree == qTree

    def fillTree(self, node: TreeNode, res: list):
        if node is None:
            return

        if node.left:
            res.append(node.left.val)
            self.fillTree(node.left, res)
        else:
            res.append(None)

        if node.right:
            res.append(node.right.val)
            self.fillTree(node.right, res)
        else:
            res.append(None)


if __name__ == "__main__":
    o = Solution()

    t1 = TreeNode.fromList([1, 2])
    t2 = TreeNode.fromList([1, None, 2])

    print(o.isSameTree(t1, t2))
