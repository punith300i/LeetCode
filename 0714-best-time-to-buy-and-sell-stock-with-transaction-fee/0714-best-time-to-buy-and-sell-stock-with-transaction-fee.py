class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        profit = 0
        bye_price = prices[0];
        
        for i in range(1,n):
            profit = max(profit, prices[i]-bye_price-fee)
            bye_price = min(bye_price, prices[i]-profit)
        
        return profit