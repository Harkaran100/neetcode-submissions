class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # do a for loop
        # in the loop have 2 points 
        # L at i + 1 and right and end of list
        # while left < right
            # calculate the sum if greater then 0 move r -1 if less move l + 1
            # if find match put in res else keep going 
        nums.sort()
        result = []
        for number in range(len(nums)):
            left = number + 1
            right = len(nums) - 1
            while right > left:
                currentSum = nums[number] + nums[left] + nums[right]
                if currentSum == 0:
                    # check for duplciate
                    if [nums[number], nums[left], nums[right]] in result:
                        left += 1
                        right -= 1
                    else:
                        result.append([nums[number], nums[left], nums[right]])
                        left += 1
                        right -= 1
                elif currentSum > 0:
                    right -= 1
                else:
                    left += 1
        return result
        