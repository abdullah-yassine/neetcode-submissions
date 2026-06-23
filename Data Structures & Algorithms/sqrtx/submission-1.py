class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        temp_ans = 0
        while left <= right:
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                temp_ans = mid
                left = mid + 1
        return temp_ans