class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # log n time o of 1 space
        left = 0
        right = len(nums) - 1
        while right >= left:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return left


        