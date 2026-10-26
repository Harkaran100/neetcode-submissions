class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make hashMap
        Count = {}
        
        for number in nums:
            if number not in Count:
                Count[number] = 0
            Count[number] += 1
        # create empty buckets/ arrays in array
        Buckets = []
        for i in range(len(nums) + 1):
            Buckets.append([])

        # place values in respective buckets
        for value, freq in Count.items():
            Buckets[freq].append(value)

        result = []

        for i in reversed(Buckets):
            for val in i:
                result.append(val)
                if len(result) == k:
                    return result

