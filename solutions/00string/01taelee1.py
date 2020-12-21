class Solution:
    def isPalindrome(self, s: str) -> bool:
        sss = ""
        for c in s:
            if c.isalnum():
                sss += c.lower()
        print(sss)
        if sss == "":
            return True
        for i in range(len(sss)):
            if sss[i] != sss[len(sss) - 1 - i]:
                return False
        return True
