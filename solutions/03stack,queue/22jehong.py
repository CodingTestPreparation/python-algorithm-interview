class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        # 며칠 남았는지 바뀌지 않는 것들은 건들지 않을거라 0으로 초기화
        result = [0] * len(T)
        
        for i, num in enumerate(T):
            while stack and num > T[stack[-1]]:
                # 지금 온도보다 낮으면 pop
                out = stack.pop()
                # result의 0을 며칠 남았는지로 변환
                result[out] = i - out
            
            stack.append(i)
        
        return result