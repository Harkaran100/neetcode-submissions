class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums) -1
       
        mid = length // 2
        left = 0
        right = length

        while left < right:
            if nums[left] < nums[right]: # sorted
                break
            mid = (left + right) // 2

            if nums[left] <= nums[mid]: # left sorted
                left = mid + 1
            else:
                right = mid
            
        start_index = left
        end_index = start_index -1

        if nums[start_index] <= target <= nums[-1]:
            left = start_index
            right = len(nums) -1
        else:
            left = 0
            right = end_index
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return -1

        



       # input array of len n, which was sorted in ascending
       #it has now been rotated 1-n times
       # return index of target else -1

        # try to solve i log n time 
        # the fact that it was sorted could be helpful
        # binary search from middle to find rotation
        # if left > mid search left else search right 
        # once we find rototation do binary search again between start and end 
        # time log n + logn space o of 1