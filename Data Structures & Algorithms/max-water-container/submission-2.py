class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0 # init left
        right = n - 1 # init right
        maxWater = 0

        #main loop
        while left < right:
            currentWater = 0

            # calculateArea
            currentWater = (right - left) * min(heights[left],heights[right])

            # which pointer moves
            if heights[left] >= heights[right]:
                right -= 1
            else:
                left +=1
        
            # compare current and max
            maxWater = max(maxWater, currentWater)

        # return
        return maxWater


        # input: array of heights
        # chose the 2 heights that allow to get most water
        # formuala height x width, do (right - left) x height of shorter of the two
        # strat 2 pointer
        # need maxWater
        # need a currentWater

        # how to iterate?? 
        # while left < right

        # how to decide which pointer moves

        # goal is most area, so have to look for highest 2 heights

        