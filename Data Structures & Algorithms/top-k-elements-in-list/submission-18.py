class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 0
            hashMap[num] += 1
        # create buckets
        buckets = []
        for i in (range(len(nums) + 1)):
            buckets.append([])

        # populate buckets
        for key in hashMap:
            bucket = hashMap[key]
            buckets[bucket].append(key)

        # populate res
        res = []
        for b in buckets[::-1]:
            for element in b:
                res.append(element)
                k -= 1
                if k == 0:
                    return res

        print(buckets)
        

