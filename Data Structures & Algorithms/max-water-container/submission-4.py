class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(heights) -1
        while left < right:
            #calculate length
            length = right - left
            #calculate height
            height = min(heights[left],heights[right])
            currentArea = length * height
            maxArea = max(maxArea,currentArea)

            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1
        return maxArea

        