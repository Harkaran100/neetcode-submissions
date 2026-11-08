class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxConsecutive = 0
        numsSet = set()

        # populate
        for i in nums:
            numsSet.add(i)
        
        for num in numsSet:
            if num-1 not in numsSet: # start
                currConsecutive = 1
                while num + 1 in numsSet:
                    currConsecutive += 1
                    num += 1
                maxConsecutive = max(maxConsecutive,currConsecutive)
        return maxConsecutive



        # check if i -1 in set? but how o keep track? 
        # try to find start of possible sequences? 
        # findthose for which i -1 not in set?