class Solution:
    def reorganizeString(self, s: str) -> str:
        # create hashmap
        strMap = {}
        for char in s:
            if char not in strMap:
                strMap[char] = 0
            strMap[char] += 1

        # make maxHeap
        maxHeap = []
        for key, freq in strMap.items():
            maxHeap.append((-freq,key))
        heapq.heapify(maxHeap)
        
        result = []
        prevStr = ""
        prevCount = 0
        # add to res operation
        while maxHeap:
            freq, key = heapq.heappop(maxHeap)
            result.append(key)
            freq += 1

            # pause reactivate clause
            if prevCount < 0:
                heapq.heappush(maxHeap,(prevCount,prevStr))
            
            # assign holder
            prevCount = freq
            prevStr = key
        resultStr = "".join(result)

        if len(resultStr) != len(s):
            return ""
        return resultStr

        # example "ccccd" 
        # hashmap: c:4, d:1
        #maxHeap = -4:c, -1:d


        