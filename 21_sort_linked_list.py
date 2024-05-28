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

    def str(self):
        return f"{self.val}" + (f", {self.next.str()}" if self.next else "]")

    def __str__(self):
        return "[" + self.str()


class Solution:

    def mergeTwoLists(self, n1: ListNode, n2: ListNode):
        """
        given that n1 n2 are sorted linked lists, merge them
        """

        if n1 == None:
            return n2
        if n2 == None:
            return n1

        if n1.val < n2.val:
            head = n1
            n1 = n1.next
        else:
            head = n2
            n2 = n2.next

        cur = head

        while n1 != None and n2 != None:
            if n1.val < n2.val:
                cur.next = n1
                cur = n1
                n1 = n1.next
            else:
                cur.next = n2
                cur = n2
                n2 = n2.next

        if n1 != None:
            cur.next = n1

        if n2 != None:
            cur.next = n2

        return head


if __name__ == "__main__":
    o = Solution()
 
    print(
        o.mergeTwoLists(
            ListNode.fromList(
                [1, ],
            ),
            ListNode.fromList([2, 3, 4, 6, 7, 8, 9]),
        )
    )


'''
In this position I was responsible for updating one of the company's legacy web app to a more modern Java web framework called Vaadins. I created and updated more than 20 functional and interactive web pages, as well as updating various backend database operations, which was on Postgres with Hibernate as ORM. I have also participated in the team's code reviews and Jira sprint planning, which to me provided a very useful insight to workings of a professional dev team.
'''
'''
At this position I was developing a desktop image and data analysis program using Python and QT for GUI, and GraphQL to communicate with backend. I have used libraries such as OpenCV and SciPy to perform data anaylsis, and create widgets to visualize results with charts and export spreadsheet data. I have also implemented an asynchronous task management system, increase system through put while keeping the codebase extendable for future development.
'''