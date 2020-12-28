# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None or head.next.next == None:
            return head
        
        curr = head
        evenhead = ListNode()
        evenheadTemp = evenhead
        
        while curr and curr.next.next:
            nextOdd = curr.next.next
            
            evenheadTemp.next = curr.next
            evenheadTemp = evenheadTemp.next
            evenheadTemp.next = None
            
            curr.next = nextOdd
            curr = nextOdd
            
            if curr.next == None:
                break
            elif curr.next.next == None:
                evenheadTemp.next = curr.next
                evenheadTemp.next.next = None
                break
                
        curr.next = evenhead.next
        return head