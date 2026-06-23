class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we are given aray piles where i is piles on that day
        # h is number of hours you have to eat the bananas
        # can choose how many bananas to eat int k
        # can eat k banans per hour, if you finish a pile cant start next till next hour

        # return minimum possible k to finish by hour h
        # first determine min and max k values
        # we know h is atleast len(piles)
        # min is len(piles)
        # max is max value in piles
        maxK = max(piles)
        left = 1
        right = maxK
        possibleK = range(left, maxK)

        

        answer = maxK
        while right >= left:
            mid = (right + left) // 2
            # calculate hours at mid
            hours = 0
            for pile in piles:
               hours += math.ceil(pile/mid)
            if hours <= h: # valid
                answer = mid
                right = mid - 1
            else: # not valid
                left = mid + 1

        return answer
        