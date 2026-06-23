class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = sum_far= cnt = 0
        best_cnt = float('inf')
        while r < len(nums):
            sum_far += nums[r]
            r += 1
            cnt += 1
            while sum_far >= target:
                best_cnt = min(best_cnt, cnt)
                sum_far -= nums[l]
                l += 1
                cnt -= 1
        if best_cnt == float('inf'):
            best_cnt = 0
        return best_cnt
