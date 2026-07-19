class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degrees = [0] * numCourses
        adjacency_list = defaultdict(list) # Course : courses that depend on Course
        for dependent, independent in prerequisites:
            degrees[dependent] += 1
            adjacency_list.setdefault(independent, set())
            adjacency_list[independent].add(dependent)
        q = deque() # bfs
        for course, degree in enumerate(degrees):
            if degree  == 0:
                q.append(course)
        order = []
        processed = 0
        while q:
            pop = q.popleft()
            for course in adjacency_list.get(pop, set()):
                degrees[course] -= 1
                if degrees[course] == 0:
                    q.append(course)
            order.append(pop)
            processed += 1
        if processed == numCourses:
            return order
        else:
            return []
        return processed