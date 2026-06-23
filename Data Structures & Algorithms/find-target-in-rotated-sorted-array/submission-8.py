class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # these are usualy binary search problems.
        # binary search will not work to find target off the bat, so i am thinking we have to do
        # an inital binary search to find rotation point
        # once we have rotation point 
        # EX. [3,4,5,6,1,2]  1 is minimum at index 4
        # we know that everything to its left is 1 sorted array
        # and everything to right another sorted array
        # check which side the target falls under, then you can do
        # binary search easily

        # find min value which is the rotation point
        # remember that it should be inclusive to right sorted array and excluded from left

        # find rotation point
        left1 = 0
        right1 = len(nums) -1
        while right1 > left1:
            mid = (right1 + left1) // 2

            # right side doesnt have roation if activates
            if nums[mid] < nums[right1]:
                right1 = mid
            else:
                left1 = mid + 1

        # both sides have sorted array
        rotation = left1
        left2 = 0
        right2 = len(nums) -1

        # which side has the target

        # right side
        if (nums[rotation] <= target <= nums[right2]):
            left2 = rotation

        #target in left side
        else:
            right2 = rotation -1

        while right2 > left2:
            mid = (right2 + left2) // 2
            if nums[mid] < target <= nums[right2]:
                left2 = mid + 1
            else:
                right2 = mid
        
        if nums[left2] == target:
            return left2
        return -1




        