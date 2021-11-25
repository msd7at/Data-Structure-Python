class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ma=-100
        mi=prices[0]
        for i in range(len(prices)):
            mi=min(prices[i],mi)
            if ma< prices[i]-mi:
                ma=prices[i]-mi
        return ma
            
