class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        pass
        # do binary search to get root
        # then split into right and left subtree
        # call dfs and return value is either the left of right subtree
        # keep doing that
        left = 0
        right = len(nums) -1
        def dfs(left,right):
            if left > right:
                return
            mid = (left + right) // 2
            root = TreeNode()
            root.val = nums[mid]
            root.left = dfs(left, mid -1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(left,right)