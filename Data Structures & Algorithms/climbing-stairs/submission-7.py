class Solution:
    def climbStairs(self, n: int) -> int:
        if n in (0,1,2):
            return n 
        dp = [0] * (n)
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i-2]
        return dp[n-1]