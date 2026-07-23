class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        sums = {0}
        for stone in stones:
            sums |= {stone + s for s in sums} # either add a stone or don't for each subset
        best = max(s for s in sums if s <= total//2)  # why total // 2? because if you look at the problem, there are two piles: plus and minus. the correct answer is the one that minimize the two difference
        return total - 2 * best
        