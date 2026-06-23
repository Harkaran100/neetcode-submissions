class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find which side is rotateed
        # first get mid
        # if mid > right min is there
        # if mid < left
        left = 0
        right = len(nums) -1
        
        mid = (left + right) // 2
        while right > left:
            if nums[mid] > nums[right]:
                left = mid + 1
                mid = (left + right) // 2
            else:
                right = mid
                mid = (left + right) // 2
        return nums[left]

        