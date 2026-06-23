
class Solution:
    def hasDuplicate(self,nums: list[int]):
        # use hashset
        hashset = set()
        for i in nums:
            if i not in hashset:
                hashset.add(i)
            else:
                return True
        return False
        