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
        oddhead = ListNode()
        oddhead.next = curr
        oddheadTemp = oddhead.next
        evenhead = ListNode()
        evenhead.next = curr.next
        evenheadTemp = evenhead.next
        
        while curr and curr.next.next:
            nextOdd = curr.next.next
            curr.next = nextOdd
            curr = nextOdd
            oddheadTemp.next = curr
            oddheadTemp = oddheadTemp.next
            evenheadTemp.next = curr.next
            evenheadTemp = evenheadTemp.next
            if curr.next == None:
                oddheadTemp.next = evenhead.next
                return oddhead.next
            elif curr.next.next == None:
                oddheadTemp.next = evenhead.next
                evenheadTemp.next = None
                return oddhead.next
                