class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1) # dp[i] = maximum product of integers that equal to i
        for t in range(n + 1):
            # dp[t] = max(t * (t - i))
            for i in range(1, t):
                dp[t] = max(i * (t - i), i * dp[t - i], dp[t])
        return dp[n]