class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1) # dp[i] = least number of perfec squares required to add up to i
        dp[0] = 0 # it takes zero squares to get to 0
        for t in range(1, n + 1):
            i = 1
            while i*i <= t:
                dp[t] = min(dp[t], dp[t - i*i] + 1)
                i += 1
        return dp[n]