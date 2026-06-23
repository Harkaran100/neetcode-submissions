class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # minheap approach
        # return the k most repeated elements, not sorted in nums.

        # create hashmap [key/number: reptition/ value]
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] += 1
         
        #minheap to store freq and number as tuples
        minheap = []

        for num, freq in hashmap.items():
            heapq.heappush(minheap, (freq,num)) # flipped because minheap created by freq

            if len(minheap) > k:
                heapq.heappop(minheap)

        result = []
        for freq, num in minheap:
            result.append(num)
        return result
        