class Solution:
    def calPoints(self, operations: List[str]) -> int:
        def isInteger(s):
            try:
                int(s)
                return True
            except ValueError:
                return False
        result = []
        for op in operations:
            if isInteger(op):
                result.append(int(op))
            elif op == '+':
                result.append(result[-1] + result[-2])
            elif op == 'D':
                result.append(result[-1]*2)
            elif op == 'C':
                result.pop()
        return sum(result)