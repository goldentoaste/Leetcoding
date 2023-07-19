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
        if self.val is None:
            return "None, "

        out = str(self.val) + ", "

        if self.left:
            out += str(self.left)
        else:
            out += "None, "
        if self.right:
            out += str(self.right)
        else:
            out += "None, "
        return out


class Solution(object):
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def helper(l, low, high):
            if low > high:
                return None

            if low == high:
                return TreeNode(l[low])

            mid = (low + high) // 2

            node = TreeNode(l[mid])
            node.left = helper(l, low, mid - 1)
            node.right = helper(l, mid + 1, high)

            return node

        return helper(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    o = Solution()

    print(o.sortedArrayToBST([-10, -3, 0, 5, 9]))
