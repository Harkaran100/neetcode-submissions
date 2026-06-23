class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) //2
            # correct case
            if nums[left] <= nums[mid] <= nums[right]:
                return nums[left]
            # rotation happened between mid and left
            elif nums[left] >= nums[mid] <= nums[right]:
                right = mid
            # rotate happened between mid and right
            elif nums[left] <= nums[mid] >= nums[right]:
                left = mid + 1
        return nums[left]

        # need to find the rotation
        # [7,1,2,3,4,5,6]
        