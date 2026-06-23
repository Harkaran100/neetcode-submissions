"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # make 2 arrays 
        # start
        start = []
        end = []
        currRoom = 0
        maxRoom = 0
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        
        s = 0
        e = 0

        while s < len(start):
            if start[s] < end[e]:
                currRoom += 1
                s += 1
            else:
                currRoom -= 1
                e += 1
            maxRoom = max(maxRoom,currRoom)
        return maxRoom









    '''def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)

        start.sort()
        end.sort()

        res = 0
        count = 0

        s = 0
        e = 0

        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1

            res = max(res, count)

        return res'''