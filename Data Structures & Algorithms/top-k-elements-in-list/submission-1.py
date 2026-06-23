class Solution:
    def topKFrequent(self,nums, k):
        #Step 1: build hashmap
        hashmap = {}
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
        # step 2: min heap
        minHeap = []
        for number, frequency in hashmap.items():
            heapq.heappush(minHeap, (frequency, number))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        result = []
        for freqency, number in minHeap:
            result.append(number)
        return result