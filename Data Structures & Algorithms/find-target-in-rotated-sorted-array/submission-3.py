class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while left < right:
            midpoint = (left + right) // 2
            if nums[midpoint] > nums[right]:
                left = midpoint + 1
            else:
                right = midpoint
        pivot = left

        if nums[pivot] <= target <= nums[-1]:
            secondLeft, secondRight = pivot, len(nums) - 1
        else:
            secondLeft, secondRight = 0, pivot - 1
        
        while secondLeft <= secondRight:
            secondMidpoint = (secondLeft + secondRight) // 2
            if nums[secondMidpoint] == target:
                return secondMidpoint
            elif target > nums[secondMidpoint]:
                secondLeft = secondMidpoint + 1
            else:
                secondRight = secondMidpoint -1
        return -1


        