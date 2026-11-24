class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       # hashMap same as before o of n time and space
       # then make a minheap where insertion and deletion is klogk where k is size of heap and the k at start is nummber of insertions
       # i can do a for loop but each time above k we pop at end pop those k and add to res there attached key 
       # this is nlogk
       # so overall time is n + nlogk + k time  so overall nlogk and space o of n + o of k so o of n
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 0
            hashMap[num] += 1
        
        # make minHeap
        minheap = []
        for key, val in hashMap.items():
            heapq.heappush(minheap,(val,key))

            if len(minheap) > k:
                heapq.heappop(minheap)
        res = []
        while minheap:
            val, key = heapq.heappop(minheap)
            res.append(key)
        return res