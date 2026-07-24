class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        half = total // 2
        checklist = [False] * (half + 1) # checklist[i] = can you have weight i with stones you have
        checklist[0] = True # 0 weight can be achieved by picking nothing
        for stone in stones:
            for j in range(half, stone - 1, -1):
                if checklist[j - stone]:
                    checklist[j] = True
        for j in range(half, -1, -1):
            if checklist[j]:
                return total - 2*j