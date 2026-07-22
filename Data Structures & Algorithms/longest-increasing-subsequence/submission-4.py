import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # o(n * n)
        # dp = [1] * len(nums)
        # for i in range(len(nums)):
        #     biggest = 1
        #     for j in range(i - 1, -1, -1):
        #         if nums[j] < nums[i] :
        #             biggest = max(biggest, dp[j] + 1)
        #     dp[i] = biggest
        # return max(dp)
        tails =[]
        for num in nums:
            idx = bisect.bisect_left(tails, num)
            if idx + 1 > len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        return len(tails)
