class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       # given input of ints, return the k most frequent 

       # brute force comes to mind is to do a pass build hashMap sort it by highest values
       # where value is the count
       # return top k

       # this will b o of n time and o of n space to build hashMap
       # sorting the hashMap by values in descending will be nlogn time
       # then o of k to return the top k

       # so overall time is o of nlogn space o of n
        hashMap = {} # num -> count
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 0
            hashMap[num] += 1

        sorted_count = dict(sorted(hashMap.items(), key=lambda item: item[1], reverse=True))

        res = list(islice(sorted_count, k))
        return res
        