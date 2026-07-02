class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = Counter(s)
        _, max_count = heap.most_common(1)[0]
        if max_count > (len(s) + 1) // 2: 
            return ""
        heap = [(-count, char) for char, count in heap.most_common()]
        heapq.heapify(heap)
        prev, result = (0, ""), ""
        while heap:
            popped = heapq.heappop(heap)
            result += popped[1]
            if -prev[0] > 1:
                heapq.heappush(heap, (prev[0] + 1, prev[1]))
            prev = popped

        return result