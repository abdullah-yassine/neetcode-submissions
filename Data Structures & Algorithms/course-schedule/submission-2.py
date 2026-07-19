class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degrees = [0] * numCourses
        adjacency_list = {} # Course : courses that depend on Course
        for dependent, independent in prerequisites:
            degrees[dependent] += 1
            adjacency_list.setdefault(independent, set())
            adjacency_list[independent].add(dependent)
        q = deque()
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
        
        
        