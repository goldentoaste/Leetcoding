from typing import List, Set, Dict, Optional


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


class Solution(object):
    def hasCycle(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: bool
        """

        # use the hare and tortoise method to detect cycle
        slow = head
        fast = head

        while True:
            if fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True


if __name__ == "__main__":
    o = Solution()
    test = ListNode.fromList([1, 2, 3, 4, 5])
    test.getByIndexReversed(1).next

    print(o.hasCycle(test))  # expect true
