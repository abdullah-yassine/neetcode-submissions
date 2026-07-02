class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted(tasks[i] + [i] for i in range(len(tasks)))
        result = [tasks[0][2]]
        limit = tasks[0][1] + tasks[0][0]
        i = 1
        heap = []
        while i < len(tasks) or heap:
            while i < len(tasks) and tasks[i][0] <= limit:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            if not heap and i < len(tasks): # empty
                limit = tasks[i][0]
                continue
            popped = heapq.heappop(heap)
            limit += popped[0]
            result.append(popped[1])
        return result
