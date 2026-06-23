class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # get rid of duplicates with hashset
        if not nums: # if empty
            return 0
        
        hashset = set(nums)

        # only look for the start of sequence
        # this can be done by see if i -1 exists in hashset, if it does skip
        # this way dont need to sort

        longest = 1
        for i in hashset:
            if (i - 1) in hashset: # not start of sequence
                continue
            else: # is start of sequence
                current = 1
                current_num = i
                while current_num + 1 in hashset:
                    current += 1
                    current_num += 1
                    longest = max(longest,current)
        return longest
        