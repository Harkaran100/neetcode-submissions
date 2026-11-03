class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # input unsorted array
        # input int k
        # return kth larget value

        # first solution that comes to mind is sort and return index k - 1 but thats not allowed would have been time nlogn
        # brute force that comes to mind is simply to k loop of n where each loop we remove lowest 
        nums.sort()
        nums.reverse()
        return nums[k -1]

        [2,3,1,5,4]
        [1,2,3,4,5]
        [5,4,3,2,1]
        