# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        currNode = head
        prevTemp = None

        while currNode:
            # backup nextNode because current node's next will be modified
            nextTemp = currNode.next
            # change current node's next to the previous one
            currNode.next = prevTemp
            # put current node to prev
            prevTemp = currNode
            # move forward
            currNode = nextTemp

        return prevTemp