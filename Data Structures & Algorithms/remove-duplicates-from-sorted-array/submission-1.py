class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in range(1,len(nums)):
            if nums[right] == nums[right-1]: # duplicate skip
                continue
            else: # unique
                nums[left] = nums[right]
                left += 1
        return left

       # increasing order
       # task: remove duplicates in place o of 1 space
       # after removing duplicates return k
       # k is unique eleents
        # 2 pointers left and right
        # left writes the unique vals one after another
        # right finds the unique vals
        # so if we see repeated val right skips past, when get to unique then left writes it and moves to next
        # we repeat until right is at end

        # o of n time o of 1 space
        # return left index at end

        