class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        self.d = defaultdict(int)
        self.dfs(root, 0 , targetSum)
        return self.res

    def dfs(self, root, res, targetSum):
        if not root:
            return
        if res + root.val == targetSum:
            self.res += 1
        res += root.val
        self.res += self.d[res - targetSum]
        self.d[res] += 1
        self.dfs(root.left, res, targetSum)
        self.dfs(root.right, res, targetSum)
        self.d[res] -= 1
