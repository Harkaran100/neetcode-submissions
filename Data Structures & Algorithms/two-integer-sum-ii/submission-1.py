class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # sorted in increasing order
        # need 2 pointers
        # can start and start and end
        # 3 cases = target done
        # greater then target decrement right
        # less then target increment left pointer
        left = 0
        right = (len(numbers) - 1)
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1,right + 1]
            elif numbers[left] + numbers[right] > target:
                right -=1
            elif numbers[left] + numbers[right] < target:
                left +=1
            