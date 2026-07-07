class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        paths = []
        nums.sort()
        def backtracking(start, sum_far):
            if sum_far == target:
                result.append(paths[:])
                return
            for i in range(start, len(nums)):
                if sum_far + nums[i] > target:
                    break
                paths.append(nums[i])
                backtracking(i, sum_far + nums[i])
                paths.pop()
        backtracking(0,0)
        return result
            
            
            