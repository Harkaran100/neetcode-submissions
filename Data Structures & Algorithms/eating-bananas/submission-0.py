class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles is piles of banans, h is how many hours you have to eat
        # return minimum you can eat per hour and eat all in h hours
        # h is atleast as great as the piles, so the maximum k can be 
        # largest pile in piles, the absolute minmum can be a 1
        # so k can range between 1 - largest pile
        # if pile is finshed cant move onto next pile till next hour

        # 2 pointers
        left = 1
        right = max(piles)
        k = max(piles) # worst case this will be k, if never updated
        while left <= right:
            mid = (right + left) // 2
            total = 0
            for p in piles:
                total += math.ceil(p / mid)
            if total <= h:
                k = min(k, mid)
                right = mid -1
            else:
                left = mid + 1
        return k
        