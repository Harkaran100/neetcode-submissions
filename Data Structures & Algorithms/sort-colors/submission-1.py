class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                if right != left:
                    tmp = nums[left]
                    nums[left] = nums[right]
                    nums[right] = tmp
                left += 1
        # now only 1 and 2 remain unordered
        for right in range(left,len(nums)):
            if nums[right] == 1:
                if right != left:
                    tmp = nums[left]
                    nums[left] = nums[right]
                    nums[right] = tmp
                left += 1
        # 2 is auto sorted

        # time is o of 2n space o of 1



        # red first 0
        # white next 1
        # blue last 2

        # can we done with 2 for loops and left and right pointers

        # in first pass
        # both left and right start at 0
        # everytime right = 0, swap with left val and move up left,
        # else just move right up