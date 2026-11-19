class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # get all values into 1 arr
        mergedNums = []
        num1, num2 = 0,0

        # compare first val of each, when one array finishes append rest of other
        while num1 < len(nums1) and num2 < len(nums2):
            if nums1[num1] >= nums2[num2]:
                mergedNums.append(nums2[num2])
                num2 += 1
            else:
                mergedNums.append(nums1[num1])
                num1 += 1
        if num1 < len(nums1):
            for i in range(num1,len(nums1)):
                mergedNums.append(nums1[i])
        else:
            for i in range(num2,len(nums2)):
                mergedNums.append(nums2[i])
        print(mergedNums)

        # check odd or even
        mergedLen = len(mergedNums)
        print(mergedLen)

        if mergedLen % 2 == 1: # odd
            print("odd active")
            mid = mergedLen // 2
            return mergedNums[mid]

        else:
            print("even active")
            mid1 = mergedLen // 2
            mid2 = (mergedLen // 2) - 1
            print(mid1,mid2)
            evenMid = (mergedNums[mid1] + mergedNums[mid2]) / 2
            return evenMid

        