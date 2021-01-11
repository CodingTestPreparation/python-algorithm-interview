# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    longestPath: int = 0
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 현재 node까지의 길이를 구하는 함수
        def lengthDFS(node: TreeNode) -> int:
            # 끝을 모르기때문에 이 조건이 필요. 끝에 도달하면 -1 반환
            if not node:
                return -1
            
            # left와 right의 길이를 각각 구한다
            left = lengthDFS(node.left)
            right = lengthDFS(node.right)
            
            # 매번 diameter를 구한다. 하지만 필요한 것은 가장 긴 diameter뿐이다.
            self.longestPath = max(self.longestPath, right + left + 2)
            # 해당 node의 길이를 구한다 (가장 아래부터의 path)
            # 좌우의 길이 중 큰 것 + 1
            longestPath = max(left, right) + 1
            
            return longestPath
            
        lengthDFS(root)
        return self.longestPath