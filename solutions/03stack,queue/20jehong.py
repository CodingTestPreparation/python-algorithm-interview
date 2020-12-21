class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '(': ')', 
            '[': ']',
            '{': '}',
            ')': -1,
            ']': -1,
            '}': -1,
            }
            
        for i, char in enumerate(s):
            if stack == []:
                stack.append(char)
            elif char == brackets[stack[-1]]:
                stack.pop()
            else:
                stack.append(char)

        return stack == []