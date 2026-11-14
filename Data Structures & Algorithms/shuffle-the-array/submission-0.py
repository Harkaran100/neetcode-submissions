class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # n is given tells us midpoint, also guanretes input is even
        array1 = nums[0:n] # not inclusive
        array2 = nums[n:len(nums)]
        print(array1)
        print(array2)

        index = 0
        result = []
        while index < len(array1):
            result.append(array1[index])
            result.append(array2[index])
            index +=1
        return result
