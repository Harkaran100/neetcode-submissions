class Solution:
    def topKFrequent(self,nums, k):
        hashmap = {}
        # create hashmap
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        # create min heap since returning k max frequent
        minHeap = []
        for value, freq in hashmap.items():
            heapq.heappush(minHeap, (freq,value))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        # return in list
        result = []
        for freq, value in minHeap:
            result.append(value)
        return result