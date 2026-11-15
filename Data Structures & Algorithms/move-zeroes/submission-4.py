class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]
                if right != left:
                    nums[right] = 0
                left += 1
        
        # two pointers
        # both start at 0
        # when right finds a non zero it we put that at left
        # at the right value we replace witha zer0
        # increment left and right also moves forward

        # [0,0,1,2,0,5]
        #[1,2L,L,0R,0,0]

        # time is o of n
        # space is o of 1
        