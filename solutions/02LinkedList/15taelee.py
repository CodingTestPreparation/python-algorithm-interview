# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
	    node = ListNode()

        while head:
            node.val = head.val
            temp_node = ListNode()
            temp_node.next = node
            node = temp_node
            head = head.next
        return node.next
