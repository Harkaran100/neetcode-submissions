class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = 0 # buy
        right = 1 # sell
        while right < len(prices): # so only until right goes till last index
            currentProfit = prices[right] - prices[left]
            maxProfit = max(maxProfit,currentProfit)
            if prices[left] > prices[right]:
                left = right
                right +=1
            else:
                right +=1
        return maxProfit
        