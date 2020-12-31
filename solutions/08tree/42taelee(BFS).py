class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        queue = [root]
        depth = 0
        
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            depth += 1
        return depth
