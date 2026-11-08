class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # need to do 2 binary searches for left most and right most

        left = -1
        right = -1

        # left
        lPointer = 0
        rPointer = len(nums) -1
        while rPointer >= lPointer:
            mid = (lPointer + rPointer) // 2
            if nums[mid] > target:
                rPointer = mid -1
            elif nums[mid] < target:
                lPointer = mid + 1
            else: # mid == target
                left = mid
                rPointer = mid -1
        # right
        lPointer = 0
        rPointer = len(nums) -1
        while rPointer >= lPointer:
            mid = (lPointer + rPointer) // 2
            if nums[mid] > target:
                rPointer = mid -1
            elif nums[mid] < target:
                lPointer = mid + 1
            else: # mid == target
                right = mid
                lPointer = mid + 1
        return [left,right]


            