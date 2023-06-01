from typing import List, Set, Dict, Optional
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val : int = val
        self.next : Optional[ListNode] = next
        
    def str(self):
        return f"{self.val}" + (f", {self.next.str()}" if self.next else "]") 
    def __str__(self):
        return "[" + self.str()
    
class Solution(object):
    def hasCycle(self, head : ListNode):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        mem = set()
        
        while head:
            if head.val in mem:
                return True
            mem.add(head.val)
            head = head.next
        
        return False


if __name__ == '__main__':
    o = Solution()
    
    head = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
    head.next.next.next.next = head.next
    
    print(o.hasCycle(head)) # expect true


    head = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
    print(o.hasCycle(head)) # expect false
