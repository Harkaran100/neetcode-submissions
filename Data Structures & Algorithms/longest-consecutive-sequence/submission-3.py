class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # build hashset
        hashset = set(nums)

        longestSeq = 1
    
        for number in hashset:
            # not start of sequence
            if number - 1 in hashset:
                continue
            currentSeq = 1
            currentNum = number
            while currentNum + 1 in hashset:
                currentSeq += 1
                currentNum += 1
            longestSeq = max(longestSeq, currentSeq)
        return longestSeq