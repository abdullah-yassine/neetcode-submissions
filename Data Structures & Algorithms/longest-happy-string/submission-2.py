class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heap = [i for i in heap if i[0]]
        heapq.heapify(heap)
        res = ""
        while heap:
            count, char = heapq.heappop(heap)
            if len(res) >= 2 and res[-1] == res[-2] == char:
                if not heap:
                    break
                count2, char2 = heapq.heappop(heap)
                res += char2
                count2 += 1
                if count2:
                    heapq.heappush(heap, (count2, char2))
                heapq.heappush(heap, (count, char))
            else:
                res += char
                count += 1
                if count:
                   heapq.heappush(heap, (count, char))
        return res 
            