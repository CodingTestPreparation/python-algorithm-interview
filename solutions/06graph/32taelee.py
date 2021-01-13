from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandsNumber = 0
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '#'
            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    print(i, j)
                    islandsNumber += 1
                    dfs(grid, i, j)
                    print(grid)
        return islandsNumber

grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
solution = Solution()
print(solution.numIslands(grid))


# 첫시도 - 실패
# from typing import List
#
# class Solution:
#     height = 0
#     width = 0
#
#     def numIslands(self, grid: List[List[str]]) -> int:
#         IslandsNumber = 0
#
#         self.height = len(grid)
#         self.width = len(grid[0])
#         visited = [[0] * self.width for _ in range(self.height)]
#         for i in range(self.height):
#             for j in range(self.width):
#                 if visited[i][j] == 1:
#                     break;
#                 if grid[i][j] == 1:
#                     IslandsNumber += 1
#                     self.checkEdge(i, j, visited, grid)
#         return IslandsNumber
#
#     def checkEdge(self, i, j, visited, grid):
#         if grid[i][j] == 0:
#             return
#         #좌우 네방향 체크해서 visited 0만들기
#         visited[i][j] = 1
#         dx = [1, -1, 0, 0]
#         dy = [0, 0, 1, -1]
#         for k in range(4):
#             new_i = i + dy[k]
#             new_j = j + dx[k]
#             print('new_i: ', new_i, 'new_j', new_j)
#             if 0 <= new_i < self.height and 0 <= new_j < self.width:
#                 print('hello')
#                 if visited[new_i][new_j] == 0:
#                     print('hi')
#                     self.checkEdge(new_i, new_j, visited, grid)
#         return
#

