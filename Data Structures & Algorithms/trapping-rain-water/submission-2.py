class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        maxLeft = 0

        # populate prefix
        for h in range(len(height)):
            prefix[h] = maxLeft # assign
            maxLeft = max(maxLeft,height[h])

        maxRight = 0
        postfix = [0] * len(height)
        # populate postfix
        for h in reversed(range(len(height))):
            postfix[h] = maxRight
            maxRight = max(maxRight,height[h])

        # populate result
        result = [0] * len(height)
        for h in range(len(height)):
            minWall = min(prefix[h],postfix[h])
            water = minWall - height[h]
            if water > 0:
                result[h] = water
        # count result
        trappedWater = 0
        for water in result:
            trappedWater += water
        return trappedWater
        






        
        
        
        
        #For each index we need max left and maxright
        # use prefix and postfix to get those
        # will be stored in 2 lists prefix and postfx
        # then in third scan go in get min from pre and post 
        # at that index do that val - index height if postive append to res at that index else 0
        # final forth scan is on results where we simply add
        