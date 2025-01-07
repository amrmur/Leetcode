class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # go through prices
        # store current num
        # if next num is bigger, profit += difference, store that next num
        # else if next num is smaller, store that next num

        if(len(prices) == 1):
            return 0

        profit = 0

        for i in range(1, len(prices)):
            if(prices[i] > prices[i-1]):
                profit += prices[i] - prices[i-1]
        
        return profit
        
        # TIME COMPLEXITY: O(n)
        # SPACE COMPLEXITY: O(1)
