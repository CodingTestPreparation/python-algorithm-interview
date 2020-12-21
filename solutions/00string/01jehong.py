class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsed  = ''
        parseRev = ''
            
        for char in s:
            if ('a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9'):
                parsed += char.lower()
                
        parseRev = parsed[::-1];
        
        if (len(parsed) == 0):
            return True
        
        return parseRev == parsed

str = "A man, a plan, a canal: Panama"
str2 = '"race a car"'
str3 = "a"
str4 = '0P'

sol = Solution()
print(sol.isPalindrome(str))
print(sol.isPalindrome(str2))
print(sol.isPalindrome(str3))
print(sol.isPalindrome(str4))
