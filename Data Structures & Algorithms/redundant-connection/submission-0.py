class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(a): # finds the root given a node and returns it
            while parents[a] != a:
                a = parents[a]
            return a

        def union(a, b): # joins two nodes with each other by setting one node's root to the other
            aRoot = find(a)
            bRoot = find(b)
            if aRoot == bRoot: # they already point to the same parent
                return False
            parents[aRoot] = bRoot
            return True
        
        parents = {}
        for a, b in edges:
            parents[a] = a
            parents[b] = b
        for a,b in edges:
            if find(a) == find(b):
                return [a, b]
            union(a, b)
        return []

        