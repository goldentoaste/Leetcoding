from typing import List, Set, Dict, Optional
null = None

class ListNode(object):
    @classmethod
    def fromList(cls, items: list):
        if not items:
            return None
        root = cls(items[0])
        cur = root
        for item in items[1:]:
            cur.next = cls(item)
            cur = cur.next
        return root

    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next

    def __getitem__(self, key: int):
        if key >= 0:
            return self.getByIndex(key)
        else:
            return self.getByIndexReversed(-key)

    def getByIndex(self, key:int):
        head = self
        for i in range(key):
            if head is None:
                raise IndexError("reached end of linked list")
            head = head.next
        return head

    def getByIndexReversed(self, key:int):
        head = self
        count = 0
        while head is not None:
            head = head.next
            count += 1

        head = self
        for _ in range(count - key):
            head = head.next
        return head

    def str(self):
        return f"{self.val}" + (f", {self.next.str()}" if self.next else "]")

    def __str__(self):
        return "LinkedList[" + self.str()

    def __repr__(self):
        return f"ListNode({self.val})"

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        [1, 2, 3, 4, 5] -> [1, 5, 2, 4, 3]
        """
        if not head:
            return head

        mem = []
        while head:
            mem.append(head)
            head = head.next

        low = 0
        high = len(mem) - 1

        dummy = ListNode()
        out = dummy
        while low <= high:
            dummy.next = mem[low]
            dummy = dummy.next

            if low != high:
                dummy.next = mem[high]
                dummy = dummy.next

            high -= 1
            low += 1

        dummy.next = None

        return out.next


if __name__ == "__main__":
    o = Solution()
    l = ListNode.fromList([1, 2, 3, 4, 5])
    print(o.reorderList(l))
