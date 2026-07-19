class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # this is bfs with cyle detection
        degrees = [0] * numCourses
        adjacency_list = defaultdict(list) # Course : courses that depend on Course
        for dependent, independent in prerequisites:
            degrees[dependent] += 1
            adjacency_list[independent].append(dependent)
        q = deque() # bfs
        for course, degree in enumerate(degrees):
            if degree  == 0:
                q.append(course)
        processed = 0
        while q:
            pop = q.popleft()
            for course in adjacency_list.get(pop, set()):
                degrees[course] -= 1
                if degrees[course] == 0:
                    q.append(course)
            processed += 1

        return processed == numCourses
        
        
        