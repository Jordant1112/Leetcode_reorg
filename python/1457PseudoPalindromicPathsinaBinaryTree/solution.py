class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.count = [0]*10
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return
        if not root.left and not root.right:
            self.count[root.val] += 1
            res = 0
            for n in self.count:
                if n % 2 == 1:
                    res += 1
            if res <= 1:
                self.res += 1
            self.count[root.val] -= 1
            return
        self.count[root.val] += 1
        self.dfs(root.left)
        self.dfs(root.right)
        self.count[root.val] -= 1
