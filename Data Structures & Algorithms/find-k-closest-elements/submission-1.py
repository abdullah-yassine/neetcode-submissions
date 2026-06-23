class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search
        left, right = 0, len(arr) - k
        while left < right:
            mid = (right + left) // 2
            print()
            if abs(arr[mid] - x) > abs(arr[mid + k] - x): # mid + k is the number just outside the limit
                left = mid + 1
            else:
                right = mid
        return arr[left : left + k]