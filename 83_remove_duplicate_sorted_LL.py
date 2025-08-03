from typing import Dict, List, Optional, Set


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

    def getByIndex(self, key: int):
        head = self
        for i in range(key):
            if head is None:
                raise IndexError("reached end of linked list")
            head = head.next
        return head

    def getByIndexReversed(self, key: int):
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
        return "[" + self.str()


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        # 2 pointer, slow and fast.
        # slow is current, fast skips dups
        slow = head
        fast = head.next

        while fast:
            if slow.val != fast.val:
                slow.next = fast
                slow = slow.next

            fast = fast.next

        slow.next = None

        return head


if __name__ == "__main__":
    o = Solution()
    print(o.deleteDuplicates(ListNode.fromList([1, 1, 2, 3, 3])))
    print(o.deleteDuplicates(ListNode.fromList([1, 1, 2, 2, 3, 23, 23])))
