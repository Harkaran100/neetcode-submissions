class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums) # heapify list
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self,val: int):
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
    
    
    # much better way would be if we 
    # only ever keep size k elemnts and make it a min heap
    # reason for miheap is because it stores minimum of list
    # so techincally if we have k elements to we can simply get the min value
    # 1,2,3,3
    #
    #     3
    #    3. 3
    #.   so when greater then k we pop
    # after we add check of greqter the k
    # if so pop else return peek[-1]
    # in init though we must trim heap to size k first to get it ready fo add method
