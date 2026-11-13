class Solution:
    def trap(self, height: List[int]) -> int:
        # postive heights
        # use 2 pointers
        # we only need maxes on both sides we compute waer using the min of those 2
        trappedWater = 0
        left = 0
        right = len(height) -1
        maxLeft = height[left]
        maxRight = height[right]
        while left <= right:
            if maxLeft >= maxRight: # compute and move right
                water = maxRight - height[right]
                trappedWater += max(0,water) # only add if positive

                # check if need to update max
                right -= 1
                maxRight = max(maxRight,height[right])
            else: # compute and move left
                water = maxLeft - height[left]
                trappedWater += max(0,water)

                # check if need to update max
                left += 1
                maxLeft = max(maxLeft,height[left])
        return trappedWater
                

        