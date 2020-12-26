# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        evenList = ListNode()
        evenHead = evenList
        root = head
        
        while head and head.next:
            evenHead.next = head.next
            head.next = head.next.next
            evenHead.next.next = None
            evenHead = evenHead.next
            head = head.next
            
        head = root
        while head.next:
            head = head.next
        head.next = evenList.next
        
        return root
