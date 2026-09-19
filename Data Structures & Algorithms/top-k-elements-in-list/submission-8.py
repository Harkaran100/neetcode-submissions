class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap = {}
        for number in nums:
            if number not in hashMap:
                hashMap[number] = 0
            hashMap[number] += 1

        maxHeap = []
        for number, frequency in hashMap.items():
            heapq.heappush(maxHeap,(-frequency,number))
        result = []
        for i in range(k):
            value = (heapq.heappop(maxHeap))
            result.append(value[1])
        return result

        
        
        # input is in array nums,  int k
        # output k most frequent elements in nums

        # what if there is a tie?

        # use hashmap
        # create maxHeap
        # pop first k into res
        # return res

        # time is o of n to populate hashMap + o of n to create maxHeap + k log n for pops
        # overall of of 2n + k log n so o of n + k log n
        # space is o of n for hashmap + of o of n for maxHeap + o of k for res
        # space is overal o of n
        