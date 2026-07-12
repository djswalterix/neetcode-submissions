class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            if prices[i]<min_so_far:
                min_so_far=prices[i]
            if max_profit<prices[i]-min_so_far:
                max_profit=prices[i]-min_so_far
        return max_profit
