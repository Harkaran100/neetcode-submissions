class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
        sortedItems = sorted(hashmap.items(), key= lambda x: x[1], reverse = True)
        solution = [item[0] for item in sortedItems[:k]]
        return solution

