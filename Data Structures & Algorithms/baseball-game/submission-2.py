class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for op in operations:
            if op not in ('+', 'D','C'):
                result.append(int(op))
            elif op == '+':
                result.append(result[-1] + result[-2])
            elif op == 'D':
                result.append(result[-1]*2)
            elif op == 'C':
                result.pop()
        return sum(result)