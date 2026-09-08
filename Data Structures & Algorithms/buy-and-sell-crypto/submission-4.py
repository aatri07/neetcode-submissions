class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        right = 0
        profit = 0
        while (right < len(prices)):
            temp_minimum = prices[right]
            if temp_minimum <= minimum:
                minimum = temp_minimum
            temp_profit = prices[right] - minimum
            if temp_profit > profit:
                profit = temp_profit
            right += 1
        
        return profit





        