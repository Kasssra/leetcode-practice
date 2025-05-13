class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        summation = 0
        while i < (len(prices)-1):
            if prices[i] < prices[i+1]:
                total = prices[i+1] - prices[i]
                summation = summation + total
                i += 1
            else:
                i += 1
                continue
        return summation