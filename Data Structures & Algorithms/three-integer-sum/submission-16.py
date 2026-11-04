class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # for loop in for loop do 2 pointer skip duplicates
        # move pointers based on the curr tripled val
        result = []
        nums.sort()
        for num in range(len(nums)):
            if num > 0 and nums[num] == nums[num -1]:
                continue
            left = num + 1
            right = len(nums) -1
            while right > left:
                tripleVal = nums[num] + nums[left] + nums[right]
                if tripleVal == 0:
                    result.append([nums[num],nums[left],nums[right]])
                    right -= 1
                    left += 1
                    
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left - 1]:
                        left += 1
                elif tripleVal > 0:
                    right -= 1
                else:
                    left += 1
        return result

        