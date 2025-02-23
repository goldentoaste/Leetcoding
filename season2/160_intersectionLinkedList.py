from tkinter import N
from typing import List, Set, Dict, Optional
from Template import ListNode


class Solution:
    def getIntersectionNode(self, A: Optional[ListNode], B: ListNode) -> bool:

        if not A or not B:
            return False

        ACur = A
        BCur = B

        while ACur != BCur:
            if ACur is None:
                ACur = B
            else:
                ACur = ACur.next

            if BCur is None:
                BCur = A
            else:
                BCur = BCur.next
                

        return ACur


if __name__ == "__main__":
    o = Solution()

    l = ListNode.fromList([1, 2, 5, 6, 3, 1, 2, 4, 6, 3, 4, 5, 6])
    l2 = ListNode.fromList([1, 2, 3, 5, 1, 5, 6, 2, 4])
    l3 = ListNode.fromList([4, 2, 34, 2, 1, 6, 7])
    
    l2[-1].next = l3
    l[-1].next = l3
    

    print(o.getIntersectionNode(l, l2))
