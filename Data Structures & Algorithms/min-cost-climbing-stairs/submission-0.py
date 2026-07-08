class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) in (0,1):
            return 0
        dp = [0] * (len(cost) + 1) # dp[i] represents the cost of reaching ith step
        for step in range(2, len(cost) + 1):
            dp[step] = min(dp[step - 1] + cost[step - 1], dp[step - 2] + cost[step - 2])
        return dp[len(cost)]
