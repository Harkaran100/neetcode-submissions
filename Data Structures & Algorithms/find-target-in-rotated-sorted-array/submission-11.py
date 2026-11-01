class Solution:
    def search(self, nums: List[int], target: int) -> int:
       # input array of len n, which was sorted in ascending
       #it has now been rotated 1-n times
       # return index of target else -1

        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1