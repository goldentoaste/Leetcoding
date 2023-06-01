from typing import List, Set, Dict


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
    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        pNode, pParents = self.findNode(root, p)
        qNode, qParents = self.findNode(root, q)

        while pNode.val != qNode.val:
            plen = len(pParents)
            qlen = len(qParents)

            if plen >= qlen:
                pNode = pParents.pop()
            if qlen >= plen:
                qNode = qParents.pop()
        return pNode.val

    def findNode(self, root: TreeNode, target):
        parents: List[TreeNode] = []
        cur = root
        while cur.val != target:
            parents.append(cur)
            if cur.val > target:
                cur = cur.left
            else:
                cur = cur.right

        return cur, parents


if __name__ == "__main__":
    o = Solution()

    tree = TreeNode(
        6,
        TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
        TreeNode(8, TreeNode(7), TreeNode(9)),
    )
    
    print(o.lowestCommonAncestor(tree, 2, 8)) #expects 6
    
    

# Definition for a binary tree node.
