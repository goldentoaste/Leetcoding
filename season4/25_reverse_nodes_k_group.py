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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
            game plan:

            create a reverse(node) func that reverse a linked list

            2 pointer, fast and slow. When fast has traveled k nodes, disconnect that segment, reverse, and reattach.
        '''

        if k == 0:
            return head

        def reverse(node : ListNode):

            prev = None
            while node:
                nextNode = node.next
                node.next = prev
                prev = node
                node = nextNode
            return prev

        dummyHead = ListNode(-1)
        current = dummyHead

        slow = head

        fast = head
        prevFast = None

        dist = 0

        while True:
            if dist < k and fast:
                dist += 1
                prevFast = fast
                fast = fast.next
            if dist == k:
                # disconnect
                # if k > 0, prev fast must be defined
                prevFast.next = None

                # reverse the segment
                reversedHead = reverse(slow)

                # slow ... prevFast is now reversed. => slow is now at end of segment

                # attach to output
                current.next = reversedHead
                current = slow

                # the current fast will be the next head to reverse from next time
                prevFast = slow
                slow = fast

                dist = 0

            if not fast:
                break

        if slow:
            # has remaining segment, must be extras
            current.next = slow
        return dummyHead.next

if __name__ == "__main__":
    o = Solution()
    l = ListNode.fromList([1, 2, 3, 4, 5, 6, 7, 8])
    print(o.reverseKGroup(l, 3))
    l2 = ListNode.fromList([1, 2])
    print(o.reverseKGroup(l2, 2))