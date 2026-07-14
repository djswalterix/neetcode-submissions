from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        leveled_tree_list=[]
        queue=deque([root])
        while queue:
            nodes=len(queue)
            leveled_list=[]
            for i in range(nodes):
                actual_node=queue.popleft()
                leveled_list.append(actual_node.val)
                if actual_node.left:
                    queue.append(actual_node.left)
                if actual_node.right:
                    queue.append(actual_node.right)
            leveled_tree_list.append(leveled_list)
        return leveled_tree_list


