# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         def height(root):
#             if not root:
#                 return -1
#             return 1 + max(height(root.left), height(root.right))
        
#         def dfs(root):
#             if root:
#                 height_left = height(root.left)
#                 height_right = height(root.right)
#                 return abs(height_left - height_right) < 2 and dfs(root.left) and dfs(root.right)
#             else:
#                 return True
#         return dfs(root)
        def height(root):
            if root:
                root.val = max(height(root.left), height(root.right)) + 1
                return root.val
            else:
                return -1
        height(root)
        def dfs(root):
            if root:
                if (root.left and root.right):
                    return abs(root.left.val - root.right.val) < 2 and dfs(root.left) and dfs(root.right)
                elif (root.left):
                    return root.val < 2 and dfs(root.left)
                elif (root.right):
                    return root.val < 2 and dfs(root.right)
                return root.val < 2
            else:
                return True
        # def p(root):
        #     if root:
        #         p(root.left)
        #         print(root.val)
        #         p(root.right)
        # p(root)
        return dfs(root)