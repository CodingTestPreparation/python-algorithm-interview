from typing import List
import heapq

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result

people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
solution = Solution()

a = solution.reconstructQueue(people)
print(a)
