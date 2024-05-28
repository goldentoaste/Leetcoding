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


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode):
        return self.treeHelper(root, subRoot, subRoot)

    def treeHelper(self, root: TreeNode, subRoot: TreeNode, original: TreeNode):
        if subRoot is None and root is None:
            return True

        if root is None or subRoot is None:
            return False

        # root matches, see if left and right side matches
        if root.val == subRoot.val and ((root.left is not None) == (subRoot.left is not None)) and ((root.right is not None) == (subRoot.right is not None)):
            return self.treeHelper(
                root.left, subRoot.left, original
            ) and self.treeHelper(root.right, subRoot.right, original)

        # root dont match, reset matching progress and try again
        return self.treeHelper(root.left, original, original) or self.treeHelper(
            root.right, original, original
        )


if __name__ == "__main__":
    o = Solution()

    t1 = TreeNode.fromList([3, 4, 5, 1, 2])
    t2 = TreeNode.fromList([4, 1, 2])

    print(o.isSubtree(t1, t2))  # expect true

    t1 = TreeNode.fromList([1, 1])
    t2 = TreeNode.fromList([ 1])

    print(o.isSubtree(t1, t2))  # expect true
