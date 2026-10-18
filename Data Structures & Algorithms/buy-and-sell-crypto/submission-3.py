class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window
        left = 0  # Buy pointer
        max_profit = 0
        
        for right in range(len(prices)):# Expand the window
            if prices[right] < prices[left]:
                left = right
                continue
            # 2. Process: Calculate the profit of the current window
            current_profit = prices[right] - prices[left]
            
            # 3. Track: Update the maximum profit found so far
            max_profit = max(max_profit, current_profit)
            
        return max_profit