from typing import List, Set, Dict, Optional


class ListNode(object):
    @classmethod
    def fromList(cls, items: list):
        if not items:
            return None
        root = cls(items[0])
        for item in items[1:]:
            root.next = cls(item)
            root = item
        return root

    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next

    def str(self):
        return f"{self.val}" + (f", {self.next.str()}" if self.next else "]")

    def __str__(self):
        return "[" + self.str()


class Solution(object):
    def reverseList(self, head : ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = []
        while head.next:
            temp.append(head.val)
            head = head.next
        out = ListNode(temp[-1])
        for item in reversed(temp[:-1]):
            node = ListNode(item)
            out.next = node
            out = node
            
        return out

if __name__ == "__main__":
    o = Solution()
