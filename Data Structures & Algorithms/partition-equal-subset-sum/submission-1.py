class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        target //= 2
        switches = [False] * (target + 1)
        switches[0] = True
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1 , -1):
                if switches[j - nums[i]]:
                    switches[j] = True
        return switches[target]