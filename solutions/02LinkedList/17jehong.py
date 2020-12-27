# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPair(self, head: ListNode) -> ListNode:
        latter = head
        former = head.next
        latter.next = None
        former.next = latter
        
        return former
    
    def getLastNode(self, head: ListNode) -> ListNode:
        curr = head
        
        while curr.next:
            curr = curr.next
        
        return curr
        
    
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        curr = head
        newHead = {}
        while curr:
            if curr == None:
                return newHead
            if curr.next == None:
                self.getLastNode(newHead).next = curr
                return newHead

            tempNext = curr.next.next
            former = self.swapPair(curr)
            
            if newHead == {}:
                newHead = former
            else:
                self.getLastNode(newHead).next = former
            
            curr = tempNext
            
        return newHead