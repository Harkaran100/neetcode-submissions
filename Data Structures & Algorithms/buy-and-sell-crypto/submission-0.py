class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        maxProfit = 0
        currentProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                currentProfit = prices[r] - prices[l]
                maxProfit = max(maxProfit, currentProfit)
            else:
                l = r
            r +=1
        return maxProfit
        # two pointers store max profit and current profit
        # if current profit is higher then max update max(run comparision each time)
        #if r < l update l =r and r+1 do this until r reaches end