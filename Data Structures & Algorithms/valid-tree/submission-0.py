class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Count the numbre of edges
        # if the num of edges equal to n - 1, then its a tree; otherwise, not a tree
        # if you have more than n-1 edges, then you have a cycle
        # if you have less than n-1 edges, its a disconnected graph
        if len(edges) != n - 1:
            return False
        numOfEdges = 0
        adjList = defaultdict(list)
        visited = set()
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        q = deque() # bfs
        if len(edges):
            q.append(edges[0][0])
            visited.add(edges[0][0])
        while q:
            pop = q.popleft()
            for neighbor in adjList[pop]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
                    numOfEdges += 1
        return numOfEdges == (n - 1)