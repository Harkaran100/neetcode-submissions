class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort list
        nums.sort()
        # pick 1 number at a time and do two sum with left and right pointers on others
        result = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            if  i > 0 and nums[i] == nums[i-1]: # duplicate
                    continue
            while left < right:
                if nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                elif nums[left] + nums[right] + nums[i] == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -=1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result