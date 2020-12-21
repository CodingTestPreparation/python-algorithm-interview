class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        new_s = s.lower()
        while (start < end):
            while not new_s[start].isalnum():
                start += 1
                if start == end:
                    return True
            while not new_s[end].isalnum():
                end -= 1
                if start == end:
                    return True
            if new_s[start] != new_s[end]:
                return False
            start += 1
            end -= 1
        return True
