"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def add(key):
            hashmap[key] = Node(key.val)
        if not node:
            return None
        hashmap = {} # old : new
        q = deque()
        q.append(node) # bfs
        add(node)
        while q:
            pop = q.popleft()
            for neighbor in pop.neighbors:
                if neighbor not in hashmap:
                    add(neighbor)
                    q.append(neighbor)
                hashmap[pop].neighbors.append(hashmap[neighbor])
        return hashmap[node]