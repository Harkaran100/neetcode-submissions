class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of max and current profit
        # init max to 0
        # use two pointers
        # edge case can be provided only 1 day, so cant make right pointer l + 1
        # have left pointer and right on same first index
        # if next point is smaller move left index to there
        # if the following is larger move right
        # each time smaller then curent min move left
        # each time larger then current max move right, right cant be behind left 
        # if left is updated right mus be updated to same index
        # calclate current profit and compare with max each time
        # o of n time and o of 1 space

        maxProfit = 0
        left = 0
        
        for right in range(len(prices)): # until right reaches end
            if prices[left] > prices[right]:
                left = right
            else:
                currentProfit = prices[right] - prices[left]
                maxProfit = max(maxProfit, currentProfit)
        return maxProfit


