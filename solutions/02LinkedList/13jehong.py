class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp = head
        value = []
        
        while(temp):
            value.append(str(temp.val))
            temp = temp.next
        
        return value[::-1] == value
