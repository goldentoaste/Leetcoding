from typing import List, Set, Dict, Optional


class Solution:
    def reorderList(self, head: Optional["ListNode"]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None or head.next.next is None:
            return

        originalHead = head
        head = head.next
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

    
        # slow is at half way pointm reverse the second half
        prev = None

        nextNode = slow.next
        slow.next = None
        slow = nextNode
        while True:
            nextNode = slow.next

            slow.next = prev
            prev = slow
            if nextNode is None:
                break
            
            slow = nextNode

        firstHalf = head

        secondHalf = slow


        idx = 1

        currentHead = originalHead
        while firstHalf is not None and secondHalf is not None:
            if idx % 2 != 0:
                currentHead.next = secondHalf
                secondHalf = secondHalf.next
            else:
                currentHead.next = firstHalf
                firstHalf = firstHalf.next

            currentHead = currentHead.next
            idx += 1

        if firstHalf:
            currentHead.next = firstHalf
            currentHead = currentHead.next

        
        if secondHalf:
            currentHead.next = secondHalf
            currentHead = currentHead.next

        
 

        
        


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
        return "[" + self.str()


if __name__ == "__main__":
    o = Solution()
    l = ListNode.fromList([1,2])
    o.reorderList(l)
    print(l)