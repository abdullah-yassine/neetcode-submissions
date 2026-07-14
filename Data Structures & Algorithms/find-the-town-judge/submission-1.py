class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        scores = [0] * (n + 1)
        for a,b in trust:
            scores[a] -= 1
            scores[b] += 1
        for idx, score in enumerate(scores):
            if score == n- 1:
                return idx
        return -1
            