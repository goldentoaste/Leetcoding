from typing import List, Set, Dict, Optional

null = None


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
        return f"TreeNode({self.val})"

    """
    Thank you :pray:
    https://stackoverflow.com/a/54074933/12471420
    """

    def insert(self, val):
        if self.val == val:
            return
        elif self.val < val:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)
        else:  # self.val > key
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
            line = "%s" % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = "%s" % self.val
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = "%s" % self.val
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = "%s" % self.val
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = (
            x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
        )
        if p < q:
            left += [n * " "] * (q - p)
        elif q < p:
            right += [m * " "] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        Concept:
        1. How to check a node is a common ancestor at all.
            + for a particular node, if root is p or q and either left/right has a p/q as child.
                + or left has p/q as child and right has p/q.
        2. How to check for the lowest common ancestor?
            + For any node, if either child is a CA, just return it without checking further.
        """

        def traverse(node: TreeNode):
            """
            traverse in in-order?
            """

            if not node:
                return None
            
            if node.val == q.val or node.val == p.val:
                # this covers 2 cases, if a child is p/q is does matter, this node must be lca
                # if neither child is p/q, then might as well treat this entire subbranch as this node
                return node
            
            # does left or right have our target?
            left = traverse(node.left)
            right = traverse(node.right)

            if not left and not right:
                # the target nodes are not a child, this node can be ignored.
                return None

            if left and right:
                return node
            
            return left if left else right

        return traverse(root)


if __name__ == "__main__":
    o = Solution()
    tree = TreeNode.fromList([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4])
    tree.display()
    lca = o.lowestCommonAncestor(tree, TreeNode(5), TreeNode(1))
    print(lca) # 3
    
    lca = o.lowestCommonAncestor(tree, TreeNode(5), TreeNode(4)) # 5
    print(lca)
