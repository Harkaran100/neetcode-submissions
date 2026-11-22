class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # was in ascending order
        # now ahs been rotated between 1-n times
        # all elements are unique in nums

        # log n solution 

        left = 0
        right = len(nums) -1

        while left < right: 
            mid = (left + right) // 2
            if nums[mid] > nums[right]: # rotation in right side
                left = mid + 1
            else:
                right = mid
        rotation = left # min value

        if nums[rotation] <= target <= nums[len(nums) -1]:
            left2 = rotation
            right2 = len(nums) -1
        elif nums[0] <= target <= nums[rotation-1]:
            left2 = 0
            right2 = rotation-1
        else:
            return -1

        while left2 <= right2:
            mid2 = (left2 + right2) // 2
            if nums[mid2] == target:
                return mid2
            elif nums[mid2] > target:
                right2 = mid2 -1
            else:
                left2 = mid2 + 1
        return -1







