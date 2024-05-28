from typing import List, Set, Dict, Optional


class ListNode(object):
    @classmethod
    def fromList(cls, items: list):
        if not items:
            return None
        root = cls(items[0])
        ini = root
        for item in items[1:]:
            root.next = cls(item)
            root = root.next
        return ini

    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next

    def str(self):
        return f"{self.val}" + (f", {self.next.str()}" if self.next else "]")

    def __str__(self):
        return "[" + self.str()

class Solution(object):
    def middleNode(self, head : ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        length = 1
        while temp.next:
            temp = temp.next
            length += 1
        temp = head
        for _ in range(length // 2):
            temp = temp.next
        return temp
        
if __name__ == "__main__":
    o = Solution()


    nodes = ListNode.fromList([1, 2, 3, 4, 5,6])
   
    print(o.middleNode(nodes))