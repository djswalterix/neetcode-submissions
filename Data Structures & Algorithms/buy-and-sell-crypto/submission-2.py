class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        cheapest_so_far=float('inf')

        for sell in range(len(prices)):
            print(prices[sell],"prices[sell]")
            print(cheapest_so_far,"cheapest_so_far")
            if prices[sell]<cheapest_so_far:
                cheapest_so_far=prices[sell]

                
            current=prices[sell]-cheapest_so_far
            print(current,"current")
            max_profit=max(max_profit,current)
            print("#################")

        return max_profit
                
                
            
        