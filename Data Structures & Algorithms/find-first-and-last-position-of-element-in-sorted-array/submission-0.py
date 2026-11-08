class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # input array of int nums in increasing order
        # given a target # return start and end index of target if exists else return [-1,-1]

        # o of n time o of n space
        startIndex = len(nums) + 1
        endIndex = -1
        flag = False
        for i in range(len(nums)):
            if nums[i] == target:
                flag =  True
                currIndex = i 
                if currIndex < startIndex:
                    startIndex = currIndex
                if currIndex > endIndex:
                    endIndex = currIndex
        
        if flag:
            return [startIndex,endIndex] 
        else:
            return [-1,-1] 