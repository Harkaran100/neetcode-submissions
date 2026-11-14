class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        pointer1 = 0
        pointer2 = n

        result = []
        while pointer1 < n:
            result.append(nums[pointer1])
            result.append(nums[pointer2])
            pointer1 += 1
            pointer2 +=1
        return result

