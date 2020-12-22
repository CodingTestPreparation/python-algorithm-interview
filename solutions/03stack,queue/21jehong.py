class Solution:
    def popPrev(self, arr: list, char: chr, sDict: dict) -> bool:
        for c in arr:
            if c == '':
                continue
            elif c < char:
                return True
            elif c > char and sDict[c] == 0:
                return False
            
        return False
    
    def removeDuplicateLetters(self, s: str) -> str:
        sDict = {}
        prevIndex = {}
        
        for char in s:
            if (char in sDict):
                sDict[char] += 1
            else:
                sDict[char] = 1
                prevIndex[char] = 0
        
        result = []
        for i, char in enumerate(s):
            if char not in result:
                result.append(char)
                prevIndex[char] = i
                sDict[char] -= 1
            elif char == result[-1]:
                result.append('')
                sDict[char] -= 1
            elif self.popPrev(result[prevIndex[char] + 1:i], char, sDict) == True:
                result[prevIndex[char]] = ''
                result.append(char)
                prevIndex[char] = i
                sDict[char] -= 1
            else:
                result.append('')
                sDict[char] -= 1

        return ''.join(result)