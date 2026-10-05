
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





class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # should nlgn in total, since the arr is getting bisected each time in each level of tree, height of tree is about lg n
        # in each level, maxIndex is called on segments of nums, so about o(n)
        def maxIndex(arr):
            peak = arr[0]
            peakIdx = 0
            for i, n in enumerate(arr):
                if n > peak:
                    peak = n
                    peakIdx = i
            return peakIdx
        
        def build(arr):
            '''
            this method will fill the missing value and call children
            '''
            if not arr:
                return None
            
            peakIdx = maxIndex(arr)

            rootNode = TreeNode(arr[peakIdx])

            left = build(arr[:peakIdx])
            right = build(arr[peakIdx + 1:])
            rootNode.left = left
            rootNode.right = right

            return rootNode

        return build(nums)


if __name__ == "__main__":
    o = Solution()
    res = o.constructMaximumBinaryTree([3,2,1,6,0,5])
    res.display()
