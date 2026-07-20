class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # put in hashset, if in hashset return true
        hashset = set()
        for number in nums:
            if number in hashset:
                return True
            hashset.add(number)
        return False
        # time is o of n space is o of m m is unique numbers 