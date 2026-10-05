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


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        gameplan, 2 pointers, slow and fast.
        fast scans the linked list to the end, slow lags by n steps.
        When fast reaches the end, remove the node at slow.
        '''

        fast = head
        slow = head
        prev = ListNode(-1)
        prev.next = head
        dummyHead = prev
        delay = n

        while fast:
            fast = fast.next
            delay -= 1
            if delay < 0:
                prev = slow
                slow = slow.next

        if delay <= 0:
            prev.next = slow.next # skip slow
            slow.next = None # remove hanging pointer

        return dummyHead.next




if __name__ == "__main__":
    o = Solution()
    l = ListNode.fromList([1, 2, 3, 4, 5])
    res = o.removeNthFromEnd(l, 2)
    print(res)

    l2 = ListNode.fromList([1])
    res = o.removeNthFromEnd(l2, 1)
    print(res)