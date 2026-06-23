class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            # one side to left or right would be sorted
            if nums[left] <= nums[mid]: # sorted in left side
                # check sorted side for target
                if nums[left] <= target <=nums[mid]:
                    right = mid -1
                else: # not in sorted side
                    left = mid + 1
            else: # target in right side
                # check sorted side for target
                if nums[mid] <= target <=nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1

                
                


        