"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:              # edge case: empty graph
            return None

        cloned = {}               # original node -> its clone

        def dfs(curr):
            # 1. BASE CASE: have I already cloned curr? if so, hand back that clone
            if curr in cloned:
                return cloned[curr]

            # 2. make the clone (value only for now — neighbors come next)
            copy = Node(curr.val)

            # 3. record it in the map BEFORE recursing (this is what kills the cycle)
            cloned[curr]=copy

            # 4. for each neighbor of curr, clone it and attach to copy's neighbors
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            # 5. return the finished clone
            return copy

        return dfs(node)