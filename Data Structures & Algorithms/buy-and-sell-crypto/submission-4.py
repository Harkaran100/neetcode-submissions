class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        left = 0
        right = left + 1
        maxProfit = 0
        while right < (len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                currProfit = prices[right] - prices[left]
                maxProfit = max(maxProfit,currProfit)
                right += 1
        return maxProfit


        