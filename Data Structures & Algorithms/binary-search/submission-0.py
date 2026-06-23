class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
        return -1



        # sorted in ascending
        # check if target in array, if it is return index, else return -1
        #solution has to be o(log n)
        # so cant do 1 pass