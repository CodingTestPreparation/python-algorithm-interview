class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket = ['(', '[', '{']
        close_bracket = [')', ']', '}']
        stack = []
        for bracket in s:
            if bracket in open_bracket:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                i = close_bracket.index(bracket)

                if stack.pop() != open_bracket[i]:
                    return False
        if len(stack) == 0:
            return True
        return False



