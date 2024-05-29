from typing import List, Set, Dict, Optional
from Template import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None
        original = head
        fast, slow = head, head

        while fast is not None:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = None
        return original


if __name__ == "__main__":
    o = Solution()
    print(o.deleteDuplicates(ListNode.fromList([1, 1, 2, 3, 3])))  # expect 1, 2, 3
