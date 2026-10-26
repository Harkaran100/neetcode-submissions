class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        if not nums:
            return perms


        for number in nums:
            new_perm = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    new = perm[:i] + [number] + perm[i:]
                    new_perm.append(new)
            perms = new_perm
        return perms
            

        