class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dynamic programming
        min_price = prices[0]
        max_pro = 0
        for sell in prices:
            max_pro = max(max_pro,sell - min_price)
            min_price = min(min_price,sell)
        return max_pro