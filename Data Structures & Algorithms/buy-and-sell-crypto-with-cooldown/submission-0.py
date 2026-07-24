class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = [-prices[0]] * len(prices)
        sold = [0] * len(prices)
        free = [0] * len(prices)

        for i in range(1, len(prices)):
            hold[i] = max(hold[i - 1], free[i - 1] - prices[i]) # hold from before and still am or free yesterday and bought today
            sold[i] = hold[i - 1] + prices[i]# sell it today 
            free[i] = max(free[i - 1], sold[i - 1]) # already free and skipped or sold yesterday
        return max(free[-1], sold[-1])