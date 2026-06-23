class Solution:
    def findMin(self, nums: List[int]) -> int:
        # nums has been rotated between 1 and n times
        # need to look for the point where rotation lies
        # this can be done by looking at left right and mid
        # if one side has rotation means other side is not rotated
        # check if right > mid if so then move right to mid
        # else move left = mid
        

        left = 0
        right = len(nums) -1
        while right > left:
            mid = (right + left) // 2
            # mid - right is sorted (check other side)
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

        