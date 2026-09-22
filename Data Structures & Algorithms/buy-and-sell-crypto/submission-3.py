class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # start both pointers at 0, until r at end
        # each time prices[r] > prices[l]
        # l pointer jumps to r at new local lowest
        # else compute max and keep incrementing right

        left = 0
        right = 0
        maxProfit = 0
        while right < len(prices)-1:
            # move pointers
            if prices[right] < prices[left]:
                left = right
            else:
                right += 1
            # compute profit
            currentProfit = prices[right] - prices[left]
            maxProfit = max(maxProfit,currentProfit)
        return maxProfit

# when left = 1, right = 4
        