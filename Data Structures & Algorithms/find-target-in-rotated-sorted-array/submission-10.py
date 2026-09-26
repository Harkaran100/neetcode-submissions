class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find start / min with binary search
        left = 0
        right = len(nums) -1
        while left < right:
            midPoint = (left + right) // 2
            if nums[midPoint] > nums[right]:
                left  = midPoint + 1
            else:
                right = midPoint
        # do second binary search from either start to end of array or start of array to start -1
        pivot = nums[left]

        if pivot <= target <= nums[-1]: # search start to end of arr
            left2 = left
            right2 = len(nums) -1
        else: # search start of arr to end
            left2 = 0
            right2 = left -1

        while left2 <= right2:
            midPoint2 = (left2 + right2) // 2
            if nums[midPoint2] == target:
                return midPoint2
            elif nums[midPoint2] < target:
                left2 = midPoint2 + 1
            else:
                right2 = midPoint2 -1
            
        return -1

            

        