# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max = 0
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(root: TreeNode):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            if (left + right > self.max):
                self.max = left + right
            return max(left, right) + 1
        
        height(root)
        return self.max
        
