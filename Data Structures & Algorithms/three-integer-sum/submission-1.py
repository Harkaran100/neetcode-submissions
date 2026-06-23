class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort
        nums.sort()
        #create result array
        result = []
        #itterate through
        for i, a in enumerate(nums):
            #skip duplicates if not first element
            if i > 0 and a == nums[i-1]:
                continue
            # define pointers
            left = i + 1
            right = (len(nums) -1)
            while left < right:
                threeSum = a + nums[left] + nums[right] # current3sum
                if threeSum > 0: # to big
                    right -=1
                elif threeSum < 0: # to small
                    left +=1
                # add to result
                else:
                    result.append([a,nums[left],nums[right]])
                    # move pointer
                    left +=1
                    while left < right and nums[left] == nums[left - 1]:
                        left +=1
        return result