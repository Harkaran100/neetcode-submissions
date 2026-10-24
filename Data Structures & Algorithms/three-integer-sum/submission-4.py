class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort list
        # for loop going through entire list
        # at each do two pointer from i + 1 to end
        # right pointer at end, if > 0 move left + 1
        # if <0 right -1
        # when ==0
        # check if already in result if not add to res
        nums.sort()
        result = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) -1
            while right > left:
                sum = nums[i] + nums[right] + nums[left]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                elif sum == 0:
                    triplet = (nums[i],nums[left],nums[right])
                    if triplet not in result: # check dup
                        result.append(triplet)
                    left += 1
                    right -= 1
        return result


                    