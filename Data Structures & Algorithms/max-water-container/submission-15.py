class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = -1
        while left < right:
            cur = min(heights[left], heights[right]) * (right - left)
            max_area = max(max_area, cur)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        cur = min(heights[left], heights[right]) * (right - left)
        max_area = max(max_area, cur)
        return max_area