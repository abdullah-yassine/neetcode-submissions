class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def isValid():
            return len(path) == k
        
        result = []
        path = []
        def backtrack(num):
            if isValid():
                result.append(path[:])
                return
            for i in range(num, n + 1):
                path.append(i)
                backtrack(i + 1)
                path.pop()
        backtrack(1)
        return result
