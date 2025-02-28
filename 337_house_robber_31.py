from typing import Dict, List, Optional, Set

from template.template import TreeNode


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def traverse(node : TreeNode):
            if not node:
                return (0,0)
            
            left1, left2 = traverse(node.left)
            right1, right2 = traverse(node.right)

            return (node.val + left2 + right2, max(left1, left2) + max(right2, right1) ) # (include val, no val)
        
        return max(traverse(root))


if __name__ == "__main__":
    o = Solution()
    print(TreeNode.fromList([3, 2, 3, None, 3, None, 1]).display())
    print(o.rob(TreeNode.fromList([3, 2, 3, None, 3, None, 1]))) # expect 7
    TreeNode.fromList([3, 4, 5, 1, 3, None, 1]).display()
    print(o.rob(TreeNode.fromList([3, 4, 5, 1, 3, None, 1])))  # expect 9


    t = TreeNode.fromList([41,37,44,24,39,42,48,1,35,38,40,None,43,46,49,0,2,30,36,None,None,None,None,None,None,45,47,None,None,None,None,None,4,29,32,None,None,None,None,None,None,3,9,26,None,31,34,None,None,7,11,25,27,None,None,33,None,6,8,10,16,None,None,None,28,None,None,5,None,None,None,None,None,15,19,None,None,None,None,12,None,18,20,None,13,17,None,None,22,None,14,None,None,21,23])
    t.display()
    print(o.rob(t))