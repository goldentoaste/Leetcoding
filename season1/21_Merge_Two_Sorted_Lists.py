from typing import List, Set, Dict, Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val : int = val
        self.next : Optional[ListNode] = next
        
    def str(self):
        return f"{self.val}" + (f", {self.next.str()}" if self.next else "]") 
    def __str__(self):
        return "[" + self.str()
        
class Solution(object):
    def mergeTwoLists(self, list1 : ListNode, list2: ListNode):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # in case one is empty, return the other one (no merge needed)
        # if both are empty, returning none is fine.
        if not list1:
            return list2
        if not list2:
            return list1
        
        l1 = list1
        l2 = list2
        
        # keep reference of head, and decide which is the head
        ini = None
        if l1.val < l2.val:
            ini = ListNode(l1.val)
            l1 = l1.next
        else: 
            ini = ListNode(l2.val)
            l2 = l2.next
        
        cur = ini
        
        # while there are more items to process
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        # when one of list is empty, just add the other one to end
        if not l1:
            cur.next = l2
        else:
            cur.next = l1

        # return head
        return ini
        
if __name__ == '__main__':
    
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    o = Solution()
    
    res = o.mergeTwoLists(l1, l2)
    print(res)