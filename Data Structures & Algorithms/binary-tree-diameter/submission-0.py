# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best_diameter=0
        def dfs_len(node):
            if not node:
                return 0
            nonlocal best_diameter
            left=dfs_len(node.left)
            right=dfs_len(node.right)
            current_diamenter=(left+right)
            best_diameter=max(best_diameter,current_diamenter)
            return max(left,right)+1
        dfs_len(root)
        return best_diameter