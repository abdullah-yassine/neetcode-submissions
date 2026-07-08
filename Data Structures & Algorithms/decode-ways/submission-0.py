class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, len(s) + 1):
            if s[i - 1] != '0':                # single digit valid (1-9)
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2:i]) <= 26:    # pair valid (10-26); int() fixes the type bug
                dp[i] += dp[i - 2]
        return dp[len(s)]