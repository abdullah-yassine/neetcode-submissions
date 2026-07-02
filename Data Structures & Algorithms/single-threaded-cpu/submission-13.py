class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted(tasks[i] + [i] for i in range(len(tasks)))
        result = []
        limit = i = 0
        heap = []
        while i < len(tasks) or heap:
            if not heap and limit < tasks[i][0]: # empty
                limit = tasks[i][0]
            while i < len(tasks) and tasks[i][0] <= limit:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            proc, idx = heapq.heappop(heap)
            limit += proc
            result.append(idx)
        return result
