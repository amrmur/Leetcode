class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min = prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - min)
            if(min > prices[i]):
                min = prices[i]
        return profit

        # SPACE COMPLEXITY: O(1)
        # TIME COMPLEXITY: O(n)
        
