class Solution:
    def threeSum(self,nums:List[int]):
        # output values not index
        # no duplicate triplets
        nums.sort()
        result = []
        seenTriplets = set()
        for num1 in range(len(nums)):
            hashset = set()
            if num1 > 0 and nums[num1] == nums[num1-1]: # check duplicates
                continue
            for num2 in range(num1 + 1,len(nums)):
                target = -(nums[num1]) + -(nums[num2])
                if target in hashset:
                    if (tuple([nums[num1],nums[num2], target])) not in seenTriplets:
                        result.append([nums[num1],nums[num2], target])
                        seenTriplets.add(tuple([nums[num1],nums[num2], target]))
                hashset.add(nums[num2])
        return result

