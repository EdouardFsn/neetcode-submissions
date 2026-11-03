class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        for p in range(len(prices)-1):
            diff = prices[right] - prices[left]
            if (diff > max_profit):
                max_profit = diff
            if (prices[left] > prices[right]):
                left = right
            right += 1
        return max_profit


        