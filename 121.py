class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        

        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if(prices[j] > prices[i]):
        #             max_profit = max(max_profit,prices[j]-prices[i])  Brute Force
        
        # return max_profit

        min_price = float('inf')

        for i in range(len(prices)):
            min_price= min(min_price,prices[i])
            max_profit = max(max_profit,prices[i]-min_price)

        return max_profit