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
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        out = ListNode()
        cur = out
        even = head
        if not even: return even
        odd = even.next
        if not odd: return even

        while even:
            # try advancing before we scramble the chain
            _even = even.next
            if _even:
                _even = _even.next

            _odd = None
            if odd:
                _odd = odd.next
                if _odd:
                    _odd = _odd.next

            # push odd
            if odd:
                cur.next = odd
                cur = cur.next
            else:
                # no odd node, do the special ending clause
                break
            # then even (even exist here)
            cur.next = even
            cur = cur.next

            # lets advance for reals now
            even = _even
            odd = _odd

        if even: 
            # this happens at end of list, there is a even, but no next odd to swap with
            cur.next = even
            cur = cur.next
        cur.next = None

        return out.next
            


if __name__ == "__main__":
    o = Solution()

    l = ListNode.fromList([1, 2, 3])

    print(o.swapPairs(l))
