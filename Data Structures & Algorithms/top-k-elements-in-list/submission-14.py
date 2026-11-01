class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            if num not in freqMap:
                freqMap[num] = 0
            freqMap[num] += 1
        buckets = []
        for i in range((len(nums) + 1)):
            buckets.append([])
        # populate buckets
        for key, freq in freqMap.items():
            buckets[freq].append(key)
        
        # now iterate backwards through buckets collecting up until k values
        res = []
        for bucket in reversed(buckets):
            for num in bucket:
                res.append(num)
            if len(res) == k:
                return res
        

