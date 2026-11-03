class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # input unsorted array
        # input int k
        # return kth larget value

        # first solution that comes to mind is sort and return index k - 1 but thats not allowed would have been time nlogn space o of 11 simply sort and reverse in place code is
        #nums.sort()
        #nums.reverse()
        #return nums[k -1]
        # brute force that comes to mind is simply to k loop of n where each loop we remove lowest 
        #for i in range(k -1):
            #maxNumber = nums[0]
            #maxIndex = 0        
            #for i in range(len(nums)):
                #if nums[i] > maxNumber:
                    #maxNumber = nums[i]
                    #maxIndex = i
            #print(nums[maxIndex])
            #del nums[maxIndex]

        #maxNumber = nums[0]
        
        #for i in range(len(nums)):
            #if nums[i] > maxNumber:
                #maxNumber = nums[i]
        #return maxNumber
            # this is o of k x o of n which in worst case can be o of n2 + o of k which can also be o of n so overall o of n2
            # space is o of 1

            # the more optiomal solution I can think of is 
            # what if make maxHeap, pop k - 1 elements and return the next element this would be o of n to create heap and o of k -1 logn for pop ooperations overall o of nlogn time compleity and o of n space for maxHeap
        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap,-num)

        for i in range(k -1):
            heapq.heappop(maxHeap)
        return -(heapq.heappop(maxHeap))


        #[2,3,1,5,4]
        #[1,2,3,4,5]
        #[5,4,3,2,1]
        