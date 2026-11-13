class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxProfit = 0
        for right in range(len(prices)):
            if prices[right] < prices[left]: # found cheaper stock
                left = right
            else:
                currProfit = prices[right] - prices[left]
                maxProfit = max(maxProfit,currProfit)
        return maxProfit
        # 2 pointers
        # left starts 0 only updated if get to lower val
        # loop is until right reaches end
        # at end loop calculate curr profit compare with max
        # when right < left move left to righ since better buying oppurtunity
        # o of n time and o of 1 space