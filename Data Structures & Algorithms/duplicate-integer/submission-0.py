class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Set = set()
        for n in nums:
            if n in Set:
                return True
            Set.add(n)
        return False
    