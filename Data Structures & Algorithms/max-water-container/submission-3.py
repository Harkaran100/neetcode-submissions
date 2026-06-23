class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # heights are ints where the i index is the height of bar at that index
        # return which 2 indexs would have the most water,(container)
        # probably need a max and current variable
        # traverse with 2 pointers
        # make them at l = 0 and r = len(heights) -1
        # while left < right:
        # calc contaier and shift the less of the two pointers

        left = 0
        right = len(heights) -1
        max_volume = 0
        while left <= right:
            volume = (right - left) * min(heights[left], heights[right])
            current_volume = volume
            max_volume = max (max_volume, current_volume)

            # which pointer to move
            if heights[left] >= heights[right]:
                right -=1
            if heights[left] < heights[right]:
                left +=1
            # which to move when they are equal?
        return max_volume
            

            