
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
                if left.val:
                    item.left = left
                    queue.append(left)
            else:
                left = None

            if l:
                right = cls(l.pop(0))
                if right.val:
                    item.right = right
                    queue.append(right)
            else:
                right = None

        return root

    def __str__(self):
        return f'TreeNode({self.val})'

    '''
    Thank you :pray:
    https://stackoverflow.com/a/54074933/12471420
    '''
    def insert(self, val):
        if self.val == val:
            return
        elif self.val < val:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)
        else: # self.val > key
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

class Solution(object):
    def isValidBST(self, root : TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        '''
        2 strats:
        1. in order traversal of the tree, check if the tree follows the right sorted order.
        2. get the max of left node, and min of right node. Verify max of left is less than min of right.
        '''

        return self.validate1(root) and self.validate2(root)

    def validate2(self, root: TreeNode):
        '''
        is a bst if max of left is still less than min of right
        '''

        def traverse( node: TreeNode):
            leftMin = float('inf')
            leftMax = float('-inf')

            rightMin = float('inf')
            rightMax = float('-inf')

            if node.left:
                left = traverse(node.left)
                if not left:
                    return None
                leftMin = left[0]
                leftMax = left[1]

            if node.right:
                right = traverse(node.right)
                if not right:
                    return None
                rightMin = right[0]
                rightMax = right[1]

            if leftMax >= node.val or rightMin <= node.val:
                return None

            return min(leftMin, node.val), max(rightMax, node.val)

        return traverse(root) is not None

    def validate1(self, root: TreeNode):
        '''
        is a bst iff in order traverse is sorted.
        '''

        last = float("-inf")
        def traverse(node: TreeNode):
            nonlocal last
            if not node:
                return True
            leftvalid = traverse(node.left)

            if not leftvalid or last >= node.val:
                return False

            last = node.val

            return traverse(node.right)

        return traverse(root)


if __name__ == "__main__":
    o = Solution()
    tree = TreeNode.fromList([5,1,4,None,None,3,6]) # not a bst
    tree.display()
    print(o.isValidBST(tree))

    tree2 = TreeNode.fromList([3, 2, 5, None, None, 4, 6])
    tree2.display()
    print(o.isValidBST(tree2))

    tree3 = TreeNode.fromList([32,26,47,19,None,None,56,None,27])
    tree3.display()
    print(o.isValidBST(tree3))