class Solution:
    def longestConsecutive(self, nums: List[int]):
        # we can check to see when a sequence starts if it has no number to its left
        # if it doesnt start building sequence
        # use set for o of 1 look up time
        hashset = set(nums)
        longest = 0
        for i in hashset:
            currentLength = 0
            # check if this is start of a sequence
            if i - 1 not in hashset:
                currentLength += 1
                nextNum = i + 1
                while nextNum in hashset:
                    currentLength +=1
                    nextNum += 1
            longest = max(longest, currentLength)
        return longest


