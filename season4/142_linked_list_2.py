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


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        for any t > k
        slow = ((t - k) mod n) + k
        fast = ((2t - k) mod n) + k
        solve for slow = fast

        ((t mod n )- (k mod n)) mod n
        = ((2t mod n)- (k mod n)) mod n
        = (((2 mod n) * (t mod n)) mod n - (k mod n)) mod n

        '''
        return 

if __name__ == "__main__":
    o = Solution()
    l = ListNode.fromList([1, 2, 3, 4, 5, 6])
    middle = l.getByIndex(2)
    end = l.getByIndexReversed(1)
    end.next = middle
    
    res = o.detectCycle(l)
    if res:
        print('cycle starts at:')
        print(res.val)
    else:
        print("no cycle")