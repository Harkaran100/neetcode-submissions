class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # small side
        self.minHeap = [] # large side
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -1 * num) # always push to small Side

        # check if valid by peeking
        if self.maxHeap and self.minHeap and (-1 * self.maxHeap[0]) > (self.minHeap[0]):
            number = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, number)

        # check for imbalance
        if len(self.maxHeap) > len(self.minHeap) + 1: # if diff > 1
            number = (-1 * heapq.heappop(self.maxHeap))
            heapq.heappush(self.minHeap, number)

        elif len(self.maxHeap) + 1 < len(self.minHeap):# if diff > 1
            number = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, number * -1)
        

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap): # odd/ median in maxHeap
            return (-1 * self.maxHeap[0]) # will be negative.need to switch back
        elif len(self.maxHeap) < len(self.minHeap): # odd/ median in minHeap
            return self.minHeap[0]
        else: # get top of each and /2
            val1 =(-1 * self.maxHeap[0])
            val2 = self.minHeap[0]
            return ((val1 + val2) / 2)


        
    
    # what if i use a max heap for first(minimum half)
    # use minheap for second(maximum half)
    # find a way to keep them both valid and once findMedian called
    # in even case read top of both multipy /2
    # in odd cae use the heap with extra eleemnt
    # findmedian will be o of 1 time
    # addnum will be o of log n