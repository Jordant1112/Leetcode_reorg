class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = 0
        self.post_order(root)
        return self.res

    def post_order(self, root):
        l = self.post_order(root.left) if root.left else root.val
        r = self.post_order(root.right) if root.right else root.val
        if l == -1001 or r == -1001:
            return -1001
        if l == r and root.val == l:
            self.res += 1
            return root.val
        return -1001
