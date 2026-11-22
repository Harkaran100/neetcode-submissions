class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1 # since we just deleted latest 
            elif num == candidate: # add to count
                count += 1
            else:
                count -= 1
        return candidate