


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
                if left.val is not None:
                    item.left = left
                    queue.append(left)
            else:
                left = None

            if l:
                right = cls(l.pop(0))
                if right.val is not None:
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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        first find total sum of the tree
        
        then traverse in in order. Since BST has the property of in-order = sorted order.
        Each node is current total, then after visit, subtract from total.
        '''
        
        def totalSum(node: TreeNode):
            if not node:
                return 0
            
            return node.val + totalSum(node.left) + totalSum(node.right)
        
        total = totalSum(root)

        def inOrder(node: TreeNode):
            nonlocal total
            if not node:
                return # no action for children of leaf.
            
            # visit left first
            inOrder(node.left)

            # process current node
            temp = node.val
            node.val = total

            # subtract to remove current node's value from total
            total -= temp

            inOrder(node.right)

        inOrder(root)
        return root


if __name__ == "__main__":
    o = Solution()
    tree = TreeNode.fromList([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
    tree.display()
    o.convertBST(tree)
    tree.display()