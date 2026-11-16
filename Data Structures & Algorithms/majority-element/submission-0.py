class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # use hashmap to count, return key of highest value
        elementCount = {}
        for num in nums:
            if num not in elementCount:
                elementCount[num] = 0
            elementCount[num] += 1
        maxElement = max(elementCount,key = elementCount.get)
        return maxElement

        