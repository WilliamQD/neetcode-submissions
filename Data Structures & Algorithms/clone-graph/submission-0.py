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
        
        node_map = {}
        queue = deque()
        queue.append(node)

        start = Node(node.val)
        node_map[node] = start

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in node_map:
                    queue.append(neighbor)
                    temp = Node(neighbor.val)
                else:
                    temp = node_map[neighbor]
                node_map[curr].neighbors.append(temp)
                node_map[neighbor] = temp            

        return start
