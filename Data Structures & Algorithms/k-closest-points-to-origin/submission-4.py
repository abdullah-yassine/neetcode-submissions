class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(pt[0]**2 + pt[1]**2, pt[0], pt[1]) for pt in points]
        ans = heapq.nsmallest(k, points)
        ans = [a[1:] for a in ans]
        return ans