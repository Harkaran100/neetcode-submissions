class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort() # k log k
        mergedInterval = [intervals[0]]
        for i in range(1,len(intervals)):
            currStart = intervals[i][0] # start
            currEnd = intervals[i][1]
            if mergedInterval[-1][0] <= currStart <= mergedInterval[-1][1]: # can be merged
                start = min(mergedInterval[-1][0],currStart)
                end = max(mergedInterval[-1][1],currEnd)
                mergedInterval[-1][0] = start
                mergedInterval[-1][1] = end
            else:
                mergedInterval.append(intervals[i])
        return mergedInterval

        
