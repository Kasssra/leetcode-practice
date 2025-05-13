class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        currentProfit = 0
        maxxProfit = 0
        for i in range(len(prices)):
            if prices[i] < cheapest:
                cheapest = prices[i]
            else:
                currentProfit = prices[i] - cheapest
                if currentProfit > maxxProfit:
                    maxxProfit = currentProfit
        
        return maxxProfit