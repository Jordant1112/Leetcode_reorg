class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.res = 0
        self.post_order(root)
        return self.res

    def post_order(self, root):
        if not root:
            return [0, 0]
        l = self.post_order(root.left)
        r = self.post_order(root.right)
        count = l[0] + r[0] + 1
        root_sum = l[1]+ r[1] + root.val
        self.res = max(self.res, 1.0 * root_sum / count)
        return [count, root_sum]
