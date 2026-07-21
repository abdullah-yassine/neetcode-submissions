class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # bfs, like pulling outer onion shells
        # we start with leaf nodes of degree 1
        # check its neighbors and subtracting their degrees by 1
        # if those degrees result in 1, we add to the leaves list
        # we stop if we have remaining < 2
        if n == 1:
            return [0]
        adjList = defaultdict(list)
        degrees = defaultdict(int)
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
            degrees[a] += 1
            degrees[b] += 1
        current_leaves = []
        for a, degree in degrees.items():
            if degree == 1:
                current_leaves.append(a)
        remaining = n
        while remaining > 2:
            remaining -= len(current_leaves)
            next_leaves = []
            for node in current_leaves:
                for neigh in adjList[node]:
                    degrees[neigh] -= 1
                    if degrees[neigh] == 1:
                        next_leaves.append(neigh)
            current_leaves = next_leaves
        return current_leaves
