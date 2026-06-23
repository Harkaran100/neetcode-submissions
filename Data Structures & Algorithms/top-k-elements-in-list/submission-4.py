class Solution:
    # create hashmap to count insntances of each integer
    # sort by descending values and return first k
    def topKFrequent(self,nums: List[int], k:int):
        hashmap = {}
        # count all in array
        for i in nums:
            # add and make count 0
            if i not in hashmap:
                hashmap[i] = 0
            # increase count
            hashmap[i] += 1
        # create a minheap of size k and return them
        minheap = []
        for value, freq in hashmap.items():
            heapq.heappush(minheap, [freq, value])
            if len(minheap) > k:
                heapq.heappop(minheap)
        result = []
        for freq, value in minheap:
            result.append(value)
        return result
            
        
        