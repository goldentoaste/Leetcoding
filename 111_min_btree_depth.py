from typing import List, Set, Dict, Optional
from Template import TreeNode
from collections import deque


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        depth = 0
        while q:
            depth += 1
            for _ in range(len(q)):
                val = q.popleft()
                left, right = val.left, val.right
                if not left and not right:
                    return depth
                if left:
                    q.append(left)
                if right:
                    q.append(right)
                    
        return depth

    def minDepth1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root, None])  # use None use boundry to check depth
        depth = 1
        while q:
            val = q.popleft()
            if val:
                left, right = val.left, val.right
                if not left and not right:

                    return depth
                if left:
                    q.append(left)
                if right:
                    q.append(right)
            else:
                depth += 1
                q.append(None)

        return depth


if __name__ == "__main__":
    o = Solution()
    tree = TreeNode.fromList([3, 9, 20, None, None, 15, 7])
    tree2 = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6, None, None)))))
    print(o.minDepth(tree2))
