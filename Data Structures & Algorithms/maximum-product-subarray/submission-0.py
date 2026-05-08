class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = local_max = local_min = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                temp = local_max
                local_max = local_min
                local_min = temp
            local_max = max(nums[i], local_max * nums[i])
            local_min = min(nums[i], local_min * nums[i])
            global_max = max(global_max, local_max)
        return global_max
