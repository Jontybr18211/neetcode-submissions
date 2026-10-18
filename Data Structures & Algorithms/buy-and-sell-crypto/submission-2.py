class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window
        left = 0  # Buy pointer
        max_profit = 0
        
        for right in range(len(prices)):  # Sell pointer (Expanding the window)
            
            # 1. Shrink/Reset: If we find a lower price, this becomes our new best buy day
            # We snap the left pointer to the right pointer, effectively starting a new window
            if prices[right] < prices[left]:
                left = right
                
            # 2. Process: Calculate the profit of the current window
            current_profit = prices[right] - prices[left]
            
            # 3. Track: Update the maximum profit found so far
            max_profit = max(max_profit, current_profit)
            
        return max_profit