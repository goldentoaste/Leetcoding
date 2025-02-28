from typing import Dict, List, Optional, Set

from template.template import TreeNode


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        # node index -> noskip, skip
        mem = [[-1, -1, 0] for _ in range(1000)]

        def traverse(node: TreeNode, skip: bool, index: int):
            if not node:
                return 0,0

            if skip:
                if mem[index][1] != -1:
                    return mem[index][1], mem[index][2]
            if not skip:
                if mem[index][0] != -1:
                    return mem[index][0], mem[index][2]
            
            

            val, leftCount = traverse(node.left, False, index + 1)
            rightVal, rightCount = traverse(node.right, False, index + leftCount + 1)
            val = val + rightVal
            
            if not skip:
                left, _ = traverse(node.left, True, index + 1)
                right, _ = traverse(node.right, True, index + leftCount + 1)
                val = max(val, left + node.val + right)

            if not node.left and not node.right:
                # leaf node
                if not skip:
                    val = node.val

            mem[index][int(skip)] = val
            mem[index][2] = leftCount + rightCount 
            
            return val, leftCount + rightCount 

        res = max(traverse(root, False, 0)[0], traverse(root, True, 0)[0])
        # nah
        return res


if __name__ == "__main__":
    o = Solution()
    print(TreeNode.fromList([3, 2, 3, None, 3, None, 1]).display())
    print(o.rob(TreeNode.fromList([3, 2, 3, None, 3, None, 1]))) # expect 7
    TreeNode.fromList([3, 4, 5, 1, 3, None, 1]).display()
    print(o.rob(TreeNode.fromList([3, 4, 5, 1, 3, None, 1])))  # expect 9


    t = TreeNode.fromList([41,37,44,24,39,42,48,1,35,38,40,None,43,46,49,0,2,30,36,None,None,None,None,None,None,45,47,None,None,None,None,None,4,29,32,None,None,None,None,None,None,3,9,26,None,31,34,None,None,7,11,25,27,None,None,33,None,6,8,10,16,None,None,None,28,None,None,5,None,None,None,None,None,15,19,None,None,None,None,12,None,18,20,None,13,17,None,None,22,None,14,None,None,21,23])
    t.display()
    print(o.rob(t))