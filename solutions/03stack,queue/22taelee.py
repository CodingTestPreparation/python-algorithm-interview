from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for i, curr in enumerate(T):
            while stack and curr > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer

#불통
# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         result = [0] * len(T)
#         for i in range(len(T)):
#             for j in range(i + 1, len(T)):
#                 if T[i] < T[j]:
#                     result[i] = j - i
#                     break
#         return result



T = [73, 74, 75, 71, 69, 72, 76, 73]

soulution = Solution()
print(soulution.dailyTemperatures(T))