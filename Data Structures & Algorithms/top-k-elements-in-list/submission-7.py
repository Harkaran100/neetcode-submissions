class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap = {}
        minHeap = []
        res = []
        
        for number in nums:
            if number not in hashMap:
                hashMap[number] = 0
            hashMap[number] += 1

        # iterate through entire hashMap
        for key, value in hashMap.items():
            # append to minheap as opposite do value,key
            heapq.heappush(minHeap,(value,key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        for key, value in minHeap:
            res.append(value)
        return res

        


        