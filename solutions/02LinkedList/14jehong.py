# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        values = []
        l1cur = l1
        l2cur = l2
        
        while(l1cur):
            values.append(l1cur.val)
            l1cur = l1cur.next
        while(l2cur):
            values.append(l2cur.val)
            l2cur = l2cur.next
        
        values.sort(reverse = True)
        nextNode = None
        for val in values:
            cur = ListNode(val)
            cur.next = nextNode
            nextNode = cur
        
        return cur