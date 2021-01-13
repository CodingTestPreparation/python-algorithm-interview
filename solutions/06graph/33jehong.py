class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        result = []
        def combine(prev, i):
            # 만약 digits의 마지막이라면 재귀 끝내기
            if i == len(digits):
                result.append(prev)
                return
                
            digit = digits[i]
            # digit이 2면 char는 a, b, c
            
            for char in mapping[digit]:
                output = prev + char
                # 다음 문자 호출
                combine(output, i + 1)
        
        # digits가 빈 경우는 따로 처리. 아니면 결과가 [""]이 나옴
        if digits == "":
            return []
        combine('', 0)

        return result