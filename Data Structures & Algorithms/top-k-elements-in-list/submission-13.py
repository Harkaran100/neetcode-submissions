class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            if num not in freqMap:
                freqMap[num] = 0
            freqMap[num] += 1
        maxHeap = []
        for key, freq in freqMap.items():
            heapq.heappush(maxHeap,(-freq, key))

        res = []
        while k > 0:
            number = heapq.heappop(maxHeap)
            res.append(number[1])
            k -= 1
        return(res)

       # input array nums and int k return k most frequent elements in a array
       # first sol that comes to mind is make hashmap sort then return first k keys but that is o nlogn time and o n space
       # i think we can do better with after hashmap make a maxheap
       # heapify takes o of n time and pop top k elements
       # pop is logn operation so klogn
       # overall time would be n + klogn time o of n + o of n space