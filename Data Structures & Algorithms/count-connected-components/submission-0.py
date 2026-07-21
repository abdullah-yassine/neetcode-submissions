class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def bfs(node):
            q = deque()
            q.append(node)
            visited.add(node)
            while q:
                pop = q.popleft()
                for neigh in adjList[pop]:
                    if neigh not in visited:
                        q.append(neigh)
                        visited.add(neigh)
            
        adjList = defaultdict(list)
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        visited = set()
        connected = 0
        for node in range(n):
            if node not in visited:
                bfs(node)
                connected += 1
        return connected

