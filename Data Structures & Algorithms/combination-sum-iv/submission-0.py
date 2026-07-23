class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1) # dp[i] represent all the ways to sum to i
        dp[0] = 1 # since we can sum to 0 by taking no numbers
        for t in range(target + 1):
            for num in nums:
                if num <= t:
                    dp[t] += dp[t - num]
        return dp[target]