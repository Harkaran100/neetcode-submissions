class Solution:
    def threeSum(self,nums:List[int]):
        # distinct indicies and values
        # loop hrough and do 2 pointer to equal 0
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i > 0:
                continue
            left = i + 1
            right = len(nums) -1
            while right > left:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                elif sum == 0:
                    triplet = [nums[i], nums[left], nums[right]]
                    result.append(triplet)
                    left += 1
                    right -= 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left -1]:
                        left += 1
        return result

        