# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([(root,0)])
        max_len = 0
        while queue:
            level_len = len(queue)
            node, level_idx = queue[0]
            while level_len > 0:
                curr_node, col_idx = queue.popleft()
                level_len -= 1
                
                if curr_node.left:
                    queue.append((curr_node.left, 2 * col_idx))
                if curr_node.right:
                    queue.append((curr_node.right, 2 * col_idx + 1))
            max_len  = max(max_len, col_idx - level_idx + 1)
        return max_len