class Solution:
    def maxArea(self, heights: List[int]) -> int:
      maxWater = 0
      currentWater = 0
      l,r = 0, len(heights) -1
      while l < r:
        height = min(heights[l], heights[r])
        width = r-l
        currentWater = height * width
        if maxWater < currentWater:
            maxWater = currentWater
        if heights[l] > heights[r]:
            r -= 1
        else:
            l += 1
      return maxWater

   


