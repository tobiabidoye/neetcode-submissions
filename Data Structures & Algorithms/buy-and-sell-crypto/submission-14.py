class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        max_profit = 0 

        for r in range(len(prices)): 
            while prices[r] < prices[l]:
                l += 1
                continue
            cur_profit = prices[r] - prices[l]
            max_profit = max(max_profit, cur_profit)
            print(max_profit)
           
        return max_profit 
            