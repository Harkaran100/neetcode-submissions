class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 solutions both are 0(n) time, firs is with prefix array, post fix and the min of those
        # second is opitimzed 2 pointer in which we keep track of both maxes and move indics and calculate per index using maxes
        
        if not height:
            return 0
        left = 0
        right = len(height) -1
        leftMax, rightMax = height[left] , height[right]
        result = 0
        while left < right:
            # 2 cases either move left or right
            if leftMax >= rightMax:
                right -= 1
                rightMax = max(rightMax, height[right])
                # calculate r index height of water
                result += rightMax - height[right]
            elif leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                # calculate l index height of water
                result += leftMax - height[left]
        return result
        

        