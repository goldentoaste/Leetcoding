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
        return "LinkedList[" + self.str()


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        dummyHead = ListNode(-1)
        current = dummyHead

        while head:

            if head.next and head.next.val == head.val:
                dup = head.val
                while head and head.val == dup:
                    head = head.next
            else:
                current.next = head
                current = current.next
                head = head.next

        current.next = None
        return dummyHead.next


if __name__ == "__main__":
    o = Solution()
    l = ListNode.fromList([1, 2, 3, 3, 3, 4, 4, 5])  # expect 1,2,5
    _l = o.deleteDuplicates(l)
    print(_l)

    l2 = ListNode.fromList([1, 1, 1, 1, 3, 4])
    print(o.deleteDuplicates(l2))
