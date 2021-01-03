from collections import deque

class Solution:
  def maxDepth(self, root: TreeNode) -> int:
    if not root:
      return 0
    
    queue = deque()
    queue.append(root)
    depth = 0
    
    while queue:
      for _ in range(len(queue)):
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
      
      depth += 1

   return depth