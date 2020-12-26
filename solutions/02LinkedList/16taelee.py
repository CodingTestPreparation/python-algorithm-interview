# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode()
        def add(l, l1, l2, carry):
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val
            if l2:
                val2 = l2.val
            temp = val1 + val2 + carry
            l.val = temp % 10
            carry = temp // 10
            l1 = l1.next
            l2 = l2.next
            if l1 or l2:
                l.next = ListNode()
                add(l.next, l1, l2, carry)
        add(l, l1, l2, 0)
        return l