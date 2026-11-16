class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # use hashmap to count, return key of highest value
        count = 0
        for i in nums:
            if count == 0:
                candidate = i
            if i == candidate: # increase vote
                count += 1
            else:
                count -= 1
        return candidate


        