class MedianFinder:

    def __init__(self):
        #maxheap(leftside)
        self.low = []
        #minheap(rightside)
        self.high = []

    def addNum(self, num: int) -> None:
        # Init case, if low is empty
        if not self.low:
            #add negative version for maxheap
            heapq.heappush(self.low, -num)
        # if num is less then max of lowheap
        elif -num >= self.low[0]:
            heapq.heappush(self.low, -num)
        # add to minheap/ high
        else:
            # no need to store as negative value in minheap
            heapq.heappush(self.high, num)
        if len(self.low) > len(self.high) + 1:
            self.rebalance()
        elif len(self.high) > len(self.low) + 1:
            self.rebalance()
        
        

    def findMedian(self) -> float:
        if len(self.low) == len(self.high):
            # negating here so negated values from before turns positive
            return ((-(self.low[0]) + self.high[0]) / 2)
        elif len(self.low) > len(self.high):
            # negating here so negated values from before turns positive
            return (-(self.low[0]))
        if len(self.low) < len(self.high):
            return self.high[0]

    def rebalance(self):
        if len(self.low) > len(self.high) + 1:
            # move one from low to high
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)
        elif len(self.high) > len(self.low):
            # move one from high to low
            val = heapq.heappop(self.high)
            heapq.heappush(self.low, -val)