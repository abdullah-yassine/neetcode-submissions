class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        def backtracking(idx, sum_far):
            if sum_far > target or idx >= len(nums):
                return
            elif sum_far == target:
                result.append(subset.copy())
                return
            
            
            # add the current element
            subset.append(nums[idx])
            backtracking(idx, sum_far + nums[idx])

            # add the next element
            subset.pop()
            backtracking(idx + 1, sum_far)

        backtracking(0, 0)
        return result
            
            
            