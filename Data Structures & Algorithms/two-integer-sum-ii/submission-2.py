class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # input is sorted array on number in increasing order
        # answer should be 1 indexd not 0.
        # can be repeated nums but we cannot use two of the same numbers
        # inital thought is use hashset check if target - i is in hashset
        # if not add i to hashset and go on. 
        # when returning add 1 to both answers to make it 1 indexed instead of 0
        # will have to create some sort of guard rail around the fact that same 
        # value canot be done twice, something like check i not in hashset and target - i = hashset value
        # however this solution isn't o(1) space as it is hashset of possibly size u where u is unique chars
        # also time complexity is o(n)

        # to have o(1) space
        # we shouldnt create a data structure that is new, so i am thinking finding answer in nums itself
        # only ds can be the list of size 2 which is result
        # approach can be 2 pointer.
        # example [1,2,3,4,5,6,7,8,9,10] target = 12
        # l = 0 r = len(s) -1 if l != r and l + r > target l += 1 if l + r < target then r -= 1
        # this is my highlevel approach

        left = 0
        right = len(numbers) -1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
