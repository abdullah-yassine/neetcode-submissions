class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        paths = []
        candidates.sort()
        def backtrack(idx, sum_far):
            if sum_far == target:
                result.append(paths[:])
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if sum_far + candidates[i] > target:
                    continue
                paths.append(candidates[i])
                backtrack(i + 1, candidates[i] + sum_far)
                paths.pop()
        backtrack(0,0)
        return result
