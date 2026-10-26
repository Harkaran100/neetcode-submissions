class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        minHeap = []
        result = []
        # populate hashMap
        for number in nums:
            if number not in hashMap:
                hashMap[number] = 0
            hashMap[number] += 1
        
        # populate minHeap to size k
        for value, freq in hashMap.items():
            heapq.heappush(minHeap,(freq,value))
            
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        while minHeap:
            pair = heapq.heappop(minHeap)
            result.append(pair[1])
        return result