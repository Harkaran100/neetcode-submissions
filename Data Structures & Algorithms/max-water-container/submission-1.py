class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l = 0
        r = len(heights) -1
        while r > l:
            currentWater = (min(heights[l],heights[r])) * (r-l)
            maxWater = max(currentWater,maxWater)
            if heights[l] > heights[r]:
                r -=1
            else:
                l +=1
        return maxWater
    
      
      
      #approach:
      # 2 pointers
      #set at each side of list
      # have a max water variable init at 0
      # recalculate each move and chose max between current and maxwater as new maxWater
      # while l < r keep moving left +=1 or r-=1 depending on whichever is smaller
      # meaning alter the lesser between heights[l] and heights[r]
      # calculate by doing (lesser between heights[l] and heights[r]) x (r-l)

   


