class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a hashmap
        # make an array of size nums (bucket sort array)
        
        # make a hashmap
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1

        buckets = [[] for  i in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        res = []

        # go from highest frequency to lowest frequency
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)

                if len(res) == k:
                    return res
        
        


        