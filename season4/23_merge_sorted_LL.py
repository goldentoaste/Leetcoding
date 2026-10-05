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


import heapq as hq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        queue = [(node.val, node) for node in lists]
        ListNode.__lt__ = lambda self, other: self.val < other.val
        hq.heapify(queue)
        dummyHead = ListNode(-1)
        current = dummyHead
        while queue:
            _, node = hq.heappop(queue)
            if node.next:
                hq.heappush(queue, (node.next.val, node.next), )
            current.next = node
            current = current.next
        return dummyHead.next


if __name__ == "__main__":
    o = Solution()
    vals = [ListNode.fromList(arr) for arr in [[1,4,5],[1,3,4],[2,6]]]
    print(o.mergeKLists(vals))
