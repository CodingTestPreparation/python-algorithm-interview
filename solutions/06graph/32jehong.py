from typing import List

# 1을 발견하면 재귀적으로 주변을 모두 0으로 변환 => 재귀가 끝나면 count++로 섬 개수 카운트
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # grid 범위를 벗어나거나 이미 0인 곳에 도달하면 해당 방향으로는 재귀 종류
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            
            # 방문한 곳은 0으로 바꾸기
            grid[i][j] = '0'
            
            # 주변 재귀
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 1인 경우 재귀 진입
                if grid[i][j] == '1':
                    dfs(i, j)
                    # 재귀가 끝나면 카운트++
                    count += 1
                    
        return count