class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n= len(nums)
        return max(self.robNormal(nums[0 : n - 1]), self.robNormal(nums[1 : n]))
    def robNormal(self, nums):
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i-2])
        return dp[len(nums) - 1]
