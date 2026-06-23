class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(weights, days, mid):
            count_days = 1 # we always start on day 1
            current_load= 0
            for w in weights:
                if w + current_load > mid:
                    count_days += 1
                    current_load = 0
                current_load += w
            return count_days <= days
        left, right = max(weights), sum(weights)
        result = right # best case we can ship everything in one day
        while left <= right:
            mid = (left + right) // 2
            if canShip(weights, days, mid): # good, but can we make it smaller
                result = mid
                right = mid - 1
            else: # too small, we need to make it bigger
                left = mid + 1
        return result 