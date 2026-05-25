class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def backtracking(idx):
            if idx >= len(nums):
                result.append(subset.copy())
                return
            
            # 1. Either append the current element
            subset.append(nums[idx])
            backtracking(idx + 1)

            # 2. NOT include the current index
            subset.pop()
            backtracking(idx + 1)
        backtracking(0)
        return result