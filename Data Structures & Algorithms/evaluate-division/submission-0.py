class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list) # A -> B with K and B -> A with 1/k
        weights = {}
        for (a,b),k in zip(equations, values):
            adjList[a].append(b)
            adjList[b].append(a)
            weights[(a,b)] = k
            weights[(b,a)] = 1/k
        result = [] # 1d
        for query in queries:
            a, b = query
            product = 1.0
            q, visited = deque(), set()
            q.append((a, product))
            end = False
            while q:
                pop, prod = q.popleft()
                for neigh in adjList[pop]:
                    if neigh not in visited:
                        local_prod = weights[(pop, neigh)] * prod
                        if neigh == b:
                            product = local_prod
                            q = deque()
                            end = True
                            break
                        q.append((neigh, local_prod))
                        visited.add(neigh)
            product = product if end else -1.0
            result.append(product)
        return result

