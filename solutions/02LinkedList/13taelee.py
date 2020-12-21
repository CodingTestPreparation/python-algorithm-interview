class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        val_array = []
        curr = head
        if curr == None:
            return True
        while curr != None:
            val_array.append(curr.val)
            print(curr.val)
            curr = curr.next
        return val_array == val_array[::-1]
