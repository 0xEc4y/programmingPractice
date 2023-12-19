class Solution(object):
    def maxProfit(self, prices):
        smallest = prices[0]
        profit = 0
        
        for num in prices:
            difference = num - smallest
            profit = max(profit, difference)
            smallest = min(smallest, num)
        
        return profit
            