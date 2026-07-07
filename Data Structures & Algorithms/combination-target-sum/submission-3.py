class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        paths = []
        def backtracking(start, sum_far):
            for i in range(start, len(nums)):
                paths.append(nums[i])
                if sum_far + nums[i] >= target:
                    if sum_far + nums[i] == target: 
                        result.append(paths[:])
                    paths.pop()
                    continue
                backtracking(i, sum_far + nums[i])
                paths.pop()
        backtracking(0,0)
        return result
            
            
            