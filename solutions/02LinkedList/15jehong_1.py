# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        values = []
        currentNode = head
        
        while (currentNode):
            values.append(currentNode.val)
            currentNode = currentNode.next
        
        returnhead = head
        for i in range(len(values)):
            head.val = values[::-1][i]
            head = head.next
            
        return returnhead