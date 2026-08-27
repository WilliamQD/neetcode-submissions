"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        
        node_map = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in node_map:
                    queue.append(neighbor)
                    node_map[neighbor] = Node(neighbor.val)
                node_map[curr].neighbors.append(node_map[neighbor])          

        return node_map[node]
