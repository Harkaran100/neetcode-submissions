class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        #input array on len n
        # was sorted in ascending order
        # has now been rotated in 1-n roatations
        # find target value in array, return index, if not return -1
        # use binary search to cut in half each time

        left = 0
        right = (len(nums) -1)
        

        # find minimum
        while right > left:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        start = left
        print(start)

        if nums[start] <= target <= nums[-1]: # check right
            left2 = start
            right2 = len(nums) -1
        elif nums[0] <= target <= nums[start -1]: # check left
            left2 = 0
            right2 = start -1

        else: # confirmed outside nums bounds
            return -1

        while right2>= left2:
            mid = (left2 + right2) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right2 = mid -1
            else:
                left2 = mid + 1
        return -1


        # [3,5,6,0,1,2] 6 is mid
        #[0,1,2] mid is 1
            
        