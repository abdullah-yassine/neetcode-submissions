class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            biggest = 1
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i] :
                    biggest = max(biggest, dp[j] + 1)
            dp[i] = biggest
        return max(dp)
